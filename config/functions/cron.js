'use strict';

/**
 * Cron config that gives you an opportunity
 * to run scheduled jobs.
 *
 * The cron format consists of:
 * [SECOND (optional)] [MINUTE] [HOUR] [DAY OF MONTH] [MONTH OF YEAR] [DAY OF WEEK]
 *
 * See more details here: https://strapi.io/documentation/v3.x/concepts/configurations.html#cron-tasks
 */

module.exports = {
  /**
   * Simple example.
   */
  '*/15 * * * *': () => {
    strapi.services.launchsync.syncLl2RecentUpcoming()
    strapi.services.eventsync.syncLl2Events()
  },
  '* * * * *': () => {
    strapi.services.launchsync.syncLl2All("https://lldev.thespacedevs.com/2.2.0/launch/?limit=100")
  }
};
