/**
 * article router
 */

import { factories } from '@strapi/strapi';

export default factories.createCoreRouter('api::article.article', {
  config: undefined,
  only: ['find', 'findOne']
});
