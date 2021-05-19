module.exports = ({ env }) => ({
  host: env('HOST', '0.0.0.0'),
  port: env.int('PORT', 1337),
  cron: {
    enabled: true
  },
  url: 'https://api.spaceflightnewsapi.net/v3',
  admin: {
    auth: {
      secret: env('ADMIN_JWT_SECRET', 'super_secret_jwt'),
    },
    url: '/',
    serveAdminPanel: false
  },
  ll_token: env('LL_TOKEN', 'get_this_token_via_patreon'),
  ll_url: env('LL_URL', 'https://ll.thespacedevs.com/2.2.0'),
  mq_host: env('MQ_HOST', 'localhost:5672'),
  mq_username: env('MQ_USERNAME', 'mq_username'),
  mq_password: env('MQ_PASSWORD', 'mq_password'),
  mq_virtualhost: env('MQ_VIRTUALHOST', 'mq_virtualhost')
});
