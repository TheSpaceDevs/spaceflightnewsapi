/**
 * article service
 */

import { factories } from '@strapi/strapi';

// @ts-ignore
export default factories.createCoreService('api::article.article', ({ strapi }) => ({
  async find(params) {
    params = { ...params, populate: ['launches', 'events', 'news_site'] }

    const { results } = await super.find(params);
    console.log(results)

    return results;
  }
}));
