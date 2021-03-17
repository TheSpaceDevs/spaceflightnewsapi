"use strict";
const amqp = require('amqp-connection-manager');

const { handleArticles, handleBlogs, handleReports } = require('./handleMessages')

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
          channel.consume('api.articles', (message) =>  handleArticles(message, channelWrapper)),
          channel.consume('api.blogs', (message) =>  handleBlogs(message, channelWrapper)),
          channel.consume('api.reports', (message) =>  handleReports(message, channelWrapper)),
        ])
      }
    });
  },
};
