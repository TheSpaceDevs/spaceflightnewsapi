'use strict';

/**
 * provider service.
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::provider.provider');
