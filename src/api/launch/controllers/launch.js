'use strict';

/**
 *  launch controller
 */

const { createCoreController } = require('@strapi/strapi').factories;

module.exports = createCoreController('api::launch.launch');
