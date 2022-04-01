module.exports = ({ env }) => ({
  auth: {
    secret: env('ADMIN_JWT_SECRET', '158ab5652085bdf2de8a2a575b34841b'),
  },
});
