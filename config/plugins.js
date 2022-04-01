module.exports = ({ env }) => ({
  email: {
    config: {
      provider: 'mailgun',
      providerOptions: {
        apiKey: env('MAILGUN_API_KEY'),
        domain: env('MAILGUN_DOMAIN'), //Required if you have an account with multiple domains
        host: env('MAILGUN_HOST', 'api.eu.mailgun.net'), //Optional. If domain region is Europe use 'api.eu.mailgun.net'
      },
      settings: {
        defaultFrom: 'derk@spaceflightnewsapi.net',
        defaultReplyTo: 'derk@spaceflightnewsapi.net',
      },
    },
  },
});
