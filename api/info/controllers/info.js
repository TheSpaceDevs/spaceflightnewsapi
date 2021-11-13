'use strict';
const { default: createStrapi } = require('strapi');
const pjson = require("../../../package.json")

/**
 * Read the documentation (https://strapi.io/documentation/developer-docs/latest/development/backend-customization.html#core-controllers)
 * to customize this controller
 */

module.exports = {
    async index(ctx) {
        const sites = []
        const result = await strapi.services["news-site"].find({}, ["name"])
        for (const i of result) {
            sites.push(i.name);
        }
        return {
            version: pjson.version,
            newsSites: sites
        };
      },
};
