'use strict';

/**
 *  article controller
 */

const {createCoreController} = require('@strapi/strapi').factories;

module.exports = createCoreController('api::article.article', ({strapi}) => ({
  async find(ctx) {
    const data = await strapi.entityService.findMany('api::article.article', {
      populate: {
        launches: true,
        events: true,
        news_site: true
      }
    });

    return data.map(article => strapi.service('api::utils.utils').sanitizeEntity(article));
  }
}));
