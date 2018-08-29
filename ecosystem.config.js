module.exports = {
  apps: [
    {
      name: 'Spaceflight News API',
      script: './server.js',
      watch: true,
      env: {
        PORT: 3001,
        NODE_ENV: 'test',
      },
      env_production: {
        PORT: 3002,
        NODE_ENV: 'production',
      },
    },
  ],
};
