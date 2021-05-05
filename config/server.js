module.exports = ({ env }) => ({
  host: env('HOST', '0.0.0.0'),
  port: env.int('PORT', 1337),
  cron: {
    enabled: true
  },
  admin: {
    auth: {
      secret: env('ADMIN_JWT_SECRET', '8c92df59c3e4b4f4ba02d43ffd909752'),
    },
  },
  ll_token: env('LL_TOKEN', 'get_this_token_via_patreon'),
  ll_url: env('LL_URL', 'https://ll.thespacedevs.com/2.2.0')
});
