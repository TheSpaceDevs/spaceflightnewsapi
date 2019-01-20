const config = require('config');

const url = config.get('SwaggerOptions.url');
const schemes = config.get('SwaggerOptions.schemes');

module.exports = {
  swaggerDefinition: {
    info: {
      description: 'The Spaceflight News API Documentation',
      title: 'Spaceflight News API',
      version: '1.0.0',
    },
    host: url,
    basePath: '/',
    produces: [
      "application/json"
    ],
    schemes: schemes,
    securityDefinitions: {
      JWT: {
        type: 'apiKey',
        in: 'header',
        name: 'Authorization',
        description: "",
      }
    }
  },
  basedir: __dirname, //app absolute path
  files: ['../routes/**/*.js'] //Path to the API handle folder
};
