/**
 * article controller
 */

import { factories } from '@strapi/strapi'

export default factories.createCoreController('api::article.article', ({ strapi }) => ({
  async find(ctx) {
    const { data } = await super.find(ctx);
    ctx.body = data
  }
}));
