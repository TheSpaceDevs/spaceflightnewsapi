module.exports = ({ env }) => ({
  defaultConnection: 'default',
  connections: {
    default: {
      connector: 'bookshelf',
      settings: {
        client: 'postgres',
        host: env('DATABASE_HOST', '127.0.0.1'),
        port: env.int('DATABASE_PORT', 5432),
        database: env('DATABASE_NAME', 'dbname'),
        username: env('DATABASE_USERNAME', 'saaccount'),
        password: env('DATABASE_PASSWORD', 'password'),
        ssl: {
          rejectUnauthorized: env.bool('DATABASE_SSL_SELF', false)
        }
      },
      options: {
        ssl: env.bool('DATABASE_SSL', false),
      }
    },
  },
});
