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
        console.error("error setting up a connection, retrying in 5 seconds")
        return setTimeout(strapi.services.amqp.connectMqService, 5000)
      }

      conn.createChannel(function (err, ch) {
        if (err) {
          console.error("error creating a channel, retrying in 5 seconds")
          return setTimeout(strapi.services.amqp.connectMqService, 5000)
        }

        ch.consume('api.articles', function (msg) {
            console.log('.....');
            console.log("Message:", msg.content.toString());
          }, {noAck: true}
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
