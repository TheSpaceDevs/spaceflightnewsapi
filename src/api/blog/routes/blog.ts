/**
 * blog router
 */

import { factories } from '@strapi/strapi';

export default factories.createCoreRouter('api::blog.blog', {
  config: undefined,
  only: ['find', 'findOne']
});
