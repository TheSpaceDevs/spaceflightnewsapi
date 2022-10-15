'use strict';

/**
 * news-site service.
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::news-site.news-site');
