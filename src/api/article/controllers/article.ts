/**
 * article controller
 */

import { factories, Strapi } from '@strapi/strapi'

export default factories.createCoreController('api::article.article', ({ strapi }: { strapi: Strapi }) => ({
  async find(ctx) {

    // @ts-ignore
    const { results } = await strapi.service('api::article.article').find(ctx)

    return results.map((entity) => {
      return strapi.service('api::utils.utils').articleSerializer(entity)
    })
  }
}));
