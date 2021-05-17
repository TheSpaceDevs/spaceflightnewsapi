"use strict";
const amqp = require('amqp-connection-manager');

const username = strapi.config.get("server.mq_username");
const password = strapi.config.get("server.mq_password");
const host = strapi.config.get("server.mq_host");
const virtualhost = strapi.config.get("server.mq_virtualhost");

/**
 * `amqp` service.
 */

module.exports = {
  connectMqService: () => {

    // Create a new connection manager
    const connection = amqp.connect([`amqp://${username}:${password}@${host}/${virtualhost}`]);

    const channelWrapper = connection.createChannel({
      json: true,
      setup: function(channel) {
        return Promise.all([
          channel.assertQueue('snapi'),
          channel.bindQueue('snapi', 'importer'),
          channel.consume('snapi', (message) =>  strapi.services.utils.saveMessage(message, channelWrapper)),
        ])
      }
    });
  },
};
