'use strict';

/**
 * provider router.
 */

const { createCoreRouter } = require('@strapi/strapi').factories;

module.exports = createCoreRouter('api::provider.provider');
