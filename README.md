![Cover](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/snapi_poster.png)

[![Website](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/badge_snapi_website.svg)](https://spaceflightnewsapi.net/)
[![Documentation](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/badge_snapi_doc.svg)](https://api.spaceflightnewsapi.net/v4/docs)
[![Version](https://img.shields.io/github/v/release/TheSpaceDevs/spaceflightnewsapi?style=for-the-badge)](https://github.com/TheSpaceDevs/spaceflightnewsapi/releases/tag/v4.0.3)
[![Discord](https://img.shields.io/badge/Discord-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/p7ntkNA)
[![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/the_snapi)
[![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://www.patreon.com/TheSpaceDevs)

# Spaceflight News API

The Spaceflight News API was created as a solution for my problem when I wanted to develop an app for Spaceflight News: many (great!) news sites with different APIs.

To make it easier for myself, I began a project that would aggregate metadata from those news sites and publish them through an API. Since there are others that might benefit from this API, I decided make the API publicly available.

There are great apps out on the internet, that are connected to services like <https://thespacedevs.com>. By making this API available to everyone, I hope to open new doors for the developers of these apps.

## Documentation 📖

The documentation is generated from the code, and can be found at <https://api.spaceflightnewsapi.net/v4/documentation>.

## Evolution 📈

### Version 2

In July 2020, Launch Library 2.0 was released, within the new <a href="https://thespacedevs.com">The Space Devs API</a> group. I've joined this group as a partner developer, and started finalizing SNAPI 2.0.

Version 2.0 of SNAPI is a rewrite of the entire API using Strapi as a backend, with custom endpoints written by me.
SNAPI 2 sets the stage for new features to come and focuses on bringing the existing features to the new format.

### Version 3

In the Spring of 2021, Strapi announced that they would retire support for MongoDB. Since SNAPI was using MongoDB as the database, this had quite a big impact.
Version 3 of the API is exactly the same as version 2 (in terms of the response), except the IDs. These changed from ObjectIDs (strings) to integers.

### Version 4
In 2023 SNAPI V4 launched, completely re-written in Python (Django) for various reasons.
Using proven libraries, this version is focussed on long-term stability and maintainability.

## Launch Library 2 integration 🚀

Starting from version 2, we now have <a href="https://thespacedevs.com/llapi">Launch Library 2 API</a> integration. This way you can easily get news related to a specific launch.
A nice to have if you want to have a "related news/launches" section in your app!

## Currently imported news sites 🌐

<details>
<summary>Expand</summary>

- AmericaSpace
- Arstechnica
- Blue Origin
- CNBC
- ESA
- ElonX
- Euronews
- European Spaceflight
- Jet Propulsion Laboratory
- NASA
- NASASpaceflight
- National Geographic
- National Space Society
- Phys
- Planetary Society
- Reuters
- Space.com
- SpaceFlight Insider
- SpaceNews
- SpacePolicyOnline.com
- SpaceX
- Spaceflight Now
- SyFy
- TechCrunch
- Teslarati
- The Drive
- The Japan Times
- The Launch Pad
- The National
- The New York Times
- The Space Devs
- The Space Review
- The Verge
- The Wall Street Journal
- United Launch Alliance
- Virgin Galactic


</details>

## Changelog 📝
<details>
<summary>Expand</summary>

# V4.0.0

- Rewritten in Python and Django.

# V3.4.0

- Package updates
- Sentry fixes

# V3.0.0

- Package updates

### V3.2.0

- Various Sentry issues fixed

### V3.1.0

- Strapi updates
- Sentry updates
- Admin interface updates

### V3.0.0

- Switch to use Postgres as database

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

</details>



## Latest News Articles 📰
- <a href="https://spacepolicyonline.com/news/final-ariane-5-takes-flight/" >🔗</a> **[SpacePolicyOnline.com]** Final Ariane 5 Takes Flight


- <a href="https://spacenews.com/ariane-5-launches-for-the-final-time/" >🔗</a> **[SpaceNews]** Ariane 5 launches for the final time


- <a href="https://www.nasaspaceflight.com/2023/07/goodbye-ariane-5/" >🔗</a> **[NASASpaceflight]** Goodbye to the Ariane 5, the ‘Swiss Knife’ of Europe’s launch industry


  - <a href="https://go4liftoff.com/launch/id/e3f8e755-0867-413a-a05a-15ca06ce7fa3" >🚀</a> **Ariane 5 ECA+ | Syracuse 4B & Heinrich Hertz (H2Sat)** from Kourou, French Guiana



- <a href="https://spacenews.com/rivada-gets-more-breathing-room-to-deploy-constellation/" >🔗</a> **[SpaceNews]** Rivada gets more breathing room to deploy constellation


- <a href="https://europeanspaceflight.com/poland-complete-acceptance-phase-for-three-space-debris-observatories/" >🔗</a> **[European Spaceflight]** Poland Complete Acceptance Phase for Three Space Debris Observatories


- <a href="https://arstechnica.com/space/2023/07/europes-venerable-ariane-5-rocket-faces-a-bittersweet-ending-on-tuesday/" >🔗</a> **[Arstechnica]** Europe’s Ariane 5 rocket to make its final launch this evening [Updated]


  - <a href="https://go4liftoff.com/launch/id/e3f8e755-0867-413a-a05a-15ca06ce7fa3" >🚀</a> **Ariane 5 ECA+ | Syracuse 4B & Heinrich Hertz (H2Sat)** from Kourou, French Guiana



- <a href="https://spacenews.com/radio-noise-from-satellite-constellations-could-interfere-with-astronomers/" >🔗</a> **[SpaceNews]** Radio noise from satellite constellations could interfere with astronomers


- <a href="https://spacenews.com/regulatory-uncertainty-as-commercial-human-spaceflight-takes-off/" >🔗</a> **[SpaceNews]** Regulatory uncertainty as commercial human spaceflight takes off


- <a href="https://tlpnetwork.com/news/2023/07/european_space_forum_returns_to_brussels" >🔗</a> **[The Launch Pad]** The European Space Forum Returns to Brussels


- <a href="https://europeanspaceflight.com/cnes-creates-space-mission-ethics-committee/" >🔗</a> **[European Spaceflight]** CNES Creates Space Mission Ethics Committee




## Latest Blog Posts 🪧

- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-june-26-july-2-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: June 26-July 2, 2023


- <a href="https://europeanspaceflight.substack.com/p/what-does-the-future-hold-for-the" >🔗</a> **[European Spaceflight]** What does the future hold for the Guiana Space Center?


- <a href="https://www.planetary.org/the-downlink/searching-the-skies-to-keep-us-all-alive" >🔗</a> **[Planetary Society]** Searching the skies to keep us all alive


- <a href="https://www.planetary.org/articles/whats-going-on-with-mars-sample-return" >🔗</a> **[Planetary Society]** What’s going on with Mars Sample Return?


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-june-19-25-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: June 19-25, 2023


- <a href="https://www.planetary.org/articles/announcing-the-2023-shoemaker-neo-grant-winners" >🔗</a> **[Planetary Society]** Announcing the 2023 Shoemaker NEO grant winners


- <a href="https://europeanspaceflight.substack.com/p/everything-you-need-to-know-about-ddb" >🔗</a> **[European Spaceflight]** Everything you need to know about Themis


- <a href="https://www.planetary.org/the-downlink/rings-and-dings" >🔗</a> **[Planetary Society]** Rings and dings


- <a href="https://blog.ulalaunch.com/blog/united-launch-alliance-successfully-launches-the-penultimate-delta-iv-heavy-rocket" >🔗</a> **[United Launch Alliance]** NROL-68: United Launch Alliance Successfully Launches the Penultimate Delta IV Heavy Rocket


- <a href="https://www.planetary.org/articles/ariel-barreiro-interview" >🔗</a> **[Planetary Society]** Marrying the arts and science in space




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230706T051616">2023-07-06 05:16:16 UTC</a>
  <br>
</div>