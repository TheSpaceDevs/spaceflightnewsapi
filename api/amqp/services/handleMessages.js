// Quite some duplicate code.
// Needs clean-up / dry-onization

const toJson = (msg) => {
  return JSON.parse(msg.content.toString())
}

module.exports = {
  handleArticles: (async (msg, channel) => {
    const message = toJson(msg);
    try {
      console.log(`saving article from mq: ${message.title}`);
      await strapi.services.article.create(message);
      await channel.ack(msg);
    } catch (e) {
      // Update an existing one with updated values. Only if from the same news site.
      // URL is mostly consitent, so using that to get the duplicate one.
      const dup = await strapi.services.article.findOne({url: message.url});
      if (message.newsSite === String(dup.newsSite._id)) {
        try {
          console.log(
            `duplicate article from mq: ${dup._id} - updating instead...`
          );
          await strapi.services.article.update(
            { _id: dup._id },
            message
          );
          await channel.ack(msg);
        } catch (e) {
          console.error("error updating article", e);
        }
      } else {
        // when there's a duplicate, but from another website
        console.error(
          `duplicate from another site found: ${message.title} ${message.newsSite}`
        );
        await channel.ack(msg);
      }
    }
  }),

  handleBlogs: (async (msg, channel) => {
    const message = toJson(msg);
    try {
      console.log(`saving blog from mq: ${message.title}`);
      await strapi.services.blog.create(message);
      await channel.ack(msg);
    } catch (e) {
      // Update an existing one with updated values. Only if from the same news site.
      // URL is mostly consitent, so using that to get the duplicate one.
      const dup = await strapi.services.blog.findOne({url: message.url});
      if (message.newsSite === String(dup.newsSite._id)) {
        try {
          console.log(
            `duplicate blog from mq: ${dup._id} - updating instead...`
          );
          await strapi.services.blog.update(
            { _id: dup._id },
            message
          );
          await channel.ack(msg);
        } catch (e) {
          console.error("error updating blog", e);
        }
      } else {
        // when there's a duplicate, but from another website
        console.error(
          `duplicate from another site found: ${message.title} ${message.newsSite}`
        );
        await channel.ack(msg);
      }
    }
  }),

  handleReports: (async (msg, channel) => {
    const message = toJson(msg);
    try {
      console.log(`saving report from mq: ${message.title}`);
      await strapi.services.report.create(message);
      await channel.ack(msg);
    } catch (e) {
      // Update an existing one with updated values. Only if from the same news site.
      // URL is mostly consitent, so using that to get the duplicate one.
      const dup = await strapi.services.report.findOne({url: message.url});
      if (message.newsSite === String(dup.newsSite._id)) {
        try {
          console.log(
            `duplicate report from mq: ${dup._id} - updating instead...`
          );
          await strapi.services.report.update(
            { _id: dup._id },
            message
          );
          await channel.ack(msg);
        } catch (e) {
          console.error("error updating report", e);
        }
      } else {
        // when there's a duplicate, but from another website
        console.error(
          `duplicate from another site found: ${message.title} ${message.newsSite}`
        );
        await channel.ack(msg);
      }
    }
  })
}
