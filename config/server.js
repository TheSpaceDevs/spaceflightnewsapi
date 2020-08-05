module.exports = ({ env }) => ({
  host: env('HOST', '0.0.0.0'),
  port: env.int('PORT', 1337),
  admin: {
    auth: {
      secret: env('ADMIN_JWT_SECRET', '5b5946bc312cb8d5734214929a18bfc6'),
    },
  },
  cron: {
    enabled: true
  }
});
