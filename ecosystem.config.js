// Optimized for pm2 deploy
const config = require('../shared/config');

module.exports = {
  apps: [
    {
      script: './server.js',
      watch: true,
      env: {
        name: 'Spaceflight News API Test',
        PORT: 3001,
        NODE_ENV: 'test',
        MONGODB_URI: config.db.uri,
      },
      env_production: {
        name: 'Spaceflight News API',
        PORT: 3002,
        NODE_ENV: 'production',
        MONGODB_URI: config.db.uri,
      },
      env_dev: {
        name: 'Spaceflight News API Dev',
        PORT: 3000,
        NODE_ENV: 'dev',
        MONGODB_URI: config.db.uri,
      },
    },
  ],
  deploy: {
    // "production" is the environment name
    production: {
      user: config.pm2.user,
      host: ['snapi'],
      ref: 'origin/master',
      repo: 'git@github.com:spaceflightnewsapi/spaceflightnewsapi.git',
      path: config.pm2.path,
      'post-deploy': 'npm install',
    },
    test: {
      user: config.pm2.user,
      host: ['snapi'],
      ref: 'origin/test',
      repo: 'git@github.com:spaceflightnewsapi/spaceflightnewsapi.git',
      path: config.pm2.path,
      'post-deploy': 'npm install',
    },
  },
};
