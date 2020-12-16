module.exports = ({ env }) => ({
  host: env('HOST', '0.0.0.0'),
  port: env.int('PORT', 1337),
  admin: {
    auth: {
      secret: env('ADMIN_JWT_SECRET'),
    },
  },
  cron: {
    enabled: true
  },
  mq_host: env('MQ_HOST'),
  mq_username: env('MQ_USERNAME'),
  mq_password: env('MQ_PASSWORD'),
  mq_virtualhost: env('MQ_VIRTUALHOST')
});
