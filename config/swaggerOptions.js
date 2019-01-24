const config = require('config');

const swaggerOptions = config.get('SwaggerOptions');

module.exports = {
  swaggerDefinition: {
    info: {
      description: 'The Spaceflight News API Documentation',
      title: 'Spaceflight News API',
      version: '1.0.0',
    },
    host: swaggerOptions.url,
    basePath: '/',
    produces: [
      "application/json"
    ],
    schemes: swaggerOptions.schemes,
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
