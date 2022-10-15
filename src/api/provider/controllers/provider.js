'use strict';

/**
 *  provider controller
 */

const { createCoreController } = require('@strapi/strapi').factories;

module.exports = createCoreController('api::provider.provider');
