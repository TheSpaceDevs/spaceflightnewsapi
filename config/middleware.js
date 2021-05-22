module.exports = {
  settings: {
    prom: {
      enabled: true,
      metricsPath: '/metrics',
      includeQueryParams: true
    },
    public: {
      defaultIndex: false
    },
    logger: {
      level: 'info',
      requests: true
    }
  }
}
