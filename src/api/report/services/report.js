'use strict';

/**
 * report service.
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::report.report');
