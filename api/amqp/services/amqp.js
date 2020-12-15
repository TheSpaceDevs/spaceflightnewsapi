'use strict';
const amqp = require('amqplib/callback_api');

const username = strapi.config.get('server.mq_username');
const password = strapi.config.get('server.mq_password');
const host = strapi.config.get('server.mq_host');
const virtualhost = strapi.config.get('server.mq_virtualhost');

/**
 * `amqp` service.
 */

module.exports = {
  connectMqService: () => {
    amqp.connect(`amqp://${username}:${password}@${host}/${virtualhost}`, function (err, conn) {
      if (err) {
        console.error(`error setting up a connection to ${host}, retrying in 5 seconds`)
        return setTimeout(strapi.services.amqp.connectMqService, 5000)
      }

      console.log(`connected to mq: ${host}`)

      conn.createChannel(function (err, ch) {
        if (err) {
          console.error("error creating a channel, retrying in 5 seconds")
          return setTimeout(strapi.services.amqp.connectMqService, 5000)
        }

        ch.consume('api.articles', async function (msg) {
          let item = JSON.parse(msg.content.toString());
          try {
            console.log('saving article from mq')
            await strapi.services.article.create(item);
            await ch.ack(msg);
          } catch (e) {
            // Update an existing one with updated values. Only if from the same news site.
            const dup = await strapi.services.article.findOne(e.keyValue);
            if (item.newsSite === String(dup.newsSite._id)) {
              try {
                console.log(`duplicate article from mq: ${dup._id} - updating instead...`)
                await strapi.services.article.update({_id: dup._id}, item);
                await ch.ack(msg);
              } catch (e) {
                console.error('error updating article', e)
              }
            } else {
              // when there's a duplicate, but from another website
              console.error(`duplicate from another site found: ${msg.content.toString()}`);
            }
          }
          }, {noAck: false}
        );

        ch.consume('api.blogs', async function (msg) {
          let item = JSON.parse(msg.content.toString());
            try {
              console.log('saving blog from mq')
              await strapi.services.blog.create(item);
              await ch.ack(msg);
            } catch (e) {
              // Update an existing one with updated values. Only if from the same news site.
              const dup = await strapi.services.blog.findOne(e.keyValue);
              if (item.newsSite === String(dup.newsSite._id)) {
                try {
                  console.log(`duplicate blog from mq: ${dup._id} - updating instead...`)
                  await strapi.services.blog.update({_id: dup._id}, item);
                  await ch.ack(msg);
                } catch (e) {
                  console.error('error updating blog', e)
                }
              } else {
                // when there's a duplicate, but from another website
                console.error(`duplicate from another site found: ${msg.content.toString()}`);
              }
            }
          }, {noAck: false}
        );

        ch.consume('api.reports', async function (msg) {
          let item = JSON.parse(msg.content.toString());

            try {
              console.log('saving report from mq')
              await strapi.services.report.create(item);
              await ch.ack(msg);
            } catch (e) {
              // Update an existing one with updated values. Only if from the same news site.
              const dup = await strapi.services.report.findOne(e.keyValue);
              if (item.newsSite === String(dup.newsSite._id)) {
                try {
                  console.log(`duplicate report from mq: ${dup._id} - updating instead...`)
                  await strapi.services.report.update({_id: dup._id}, item);
                  await ch.ack(msg);
                } catch (e) {
                  console.error('error updating report', e)
                }
              } else {
                // when there's a duplicate, but from another website
                console.error(`duplicate from another site found: ${msg.content.toString()}`);
              }
            }
          }, {noAck: false}
        );
      });

      conn.on("error", function (err) {
        console.error("mq error", err.message);
      });

      conn.on("close", function () {
        console.error("connection closed, retrying in 10 seconds");
        return setTimeout(strapi.services.amqp.connectMqService, 10000);
      });
    });
  }
};
