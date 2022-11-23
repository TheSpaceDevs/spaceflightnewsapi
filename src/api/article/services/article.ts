/**
 * article service
 */

import { factories, Strapi } from '@strapi/strapi';

// @ts-ignore
export default factories.createCoreService('api::article.article', ({ strapi }: { strapi: Strapi }) => ({
  async find(params) {
    params = { ...params, populate: ['launches', 'events', 'news_site'] }

    return super.find(params);
  }
}));
