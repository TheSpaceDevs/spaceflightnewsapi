'use strict';

/**
 * launch service.
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::launch.launch');
