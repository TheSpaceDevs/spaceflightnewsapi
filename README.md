![GitHub package.json version (branch)](https://img.shields.io/github/package-json/v/spaceflightnewsapi/spaceflightnewsapi/main)
![GitHub package.json version (branch)](https://img.shields.io/github/package-json/v/spaceflightnewsapi/spaceflightnewsapi/development)
![Uptime Robot ratio (30 days)](https://img.shields.io/uptimerobot/ratio/m782215986-8b4d4ce5cf97cc49945e10b8)

# Spacelaunch News API

Spacelaunch News API was created as a solution for my problem when I wanted to develop an app for Spaceflight News: many (great!) news sites with different API's.

To make it easier for myself, I began a project that would aggegrate metadata from those news sites and publish them through an API. Since there are others that might benefit from this API, I decided make the API publicly available.

There are great apps out on the internet, that are connected to services like <https://www.launchlibrary.net/>. By making this API available to everyone, I hope to open new doors for the developers of these apps.

## Documentation

The documentation is generated from the code, and can be found at <https://www.spaceflightnewsapi.net/documentation>.

## Version 2

In Juli 2020, Launch Library 2.0 was released, within the new The Space Devs group. I've joined this group as a partner developer, and started finalizing SNAPI 2.0.

Version 2.0 of SNAPI is a rewrite of the enitre API. It's using the amazing Strapi as a backend, with custom endpoints written by me.
SNAPI 2 sets the stage for new features to come. 2.0 focuses on bringing the existing features to the new format.

## Launch Library 2 integration

Starting from version 2, we now have Launch Library 2 integration. This way you can easily get news related to a specific launch.
A nice to have if you want to have a "related news/launches" section in your app!

## Currently imported news sites

- Nasaspaceflight,
- Spacex,
- Spaceflightnow,
- Space.com,
- Spacenews,
- Nasa,
- Phys,
- Arstechnica,
- Blueorigin,
- Spaceflightinsider,
- Thejapantimes,
- Theverge,
- Teslarati,
- Elonx,
- Virgingalactic,
- Esa

## Currently imported blog sites

- Planetary Society
- National Space Society

## Changelog

### V2.3.0
- The lost "article per (LL2) event" endpoint is back
- Changed the G4L logo on the site
- Added Sentry again, via the new Strapi plugin
- Changed from amqplib to amqp-connection-manager
- Updated to Strapi 3.5.3

### v2.2.0

- Dependency updates
- Code cleanup
- Admin side of things

### v2.1.0

- Backend changes on how new content is processed
- Package updates

### v2.0.0

- Complete rewrite of the app, focusing on existing features
