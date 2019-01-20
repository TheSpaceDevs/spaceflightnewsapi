module.exports = {
  swaggerDefinition: {
    info: {
      description: 'The Spaceflight News API Documentation',
      title: 'Spaceflight News API',
      version: '1.0.0',
    },
    host: 'localhost:3000',
    basePath: '/',
    produces: [
      "application/json"
    ],
    schemes: ['http','https'],
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
