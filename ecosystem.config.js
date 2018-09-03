// Optimized for pm2 deploy
const config = require('../config');

module.exports = {
  apps: [
    {
      name: 'Spaceflight News API',
      script: './server.js',
      watch: true,
      env: {
        PORT: 3001,
        NODE_ENV: 'test',
        MONGODB_URI: config.db.uri,
      },
      env_production: {
        PORT: 3002,
        NODE_ENV: 'production',
        MONGODB_URI: config.db.uri,
      },
      env_dev: {
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
