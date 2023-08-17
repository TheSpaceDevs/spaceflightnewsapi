![Cover](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/snapi_poster.png)

[![Website](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/badge_snapi_website.svg)](https://spaceflightnewsapi.net/)
[![Documentation](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/badge_snapi_doc.svg)](https://api.spaceflightnewsapi.net/v4/docs)
[![Version](https://img.shields.io/github/v/release/TheSpaceDevs/spaceflightnewsapi?style=for-the-badge)](https://github.com/TheSpaceDevs/spaceflightnewsapi/releases/tag/v4.0.4)
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
- <a href="https://www.cnbc.com/2023/08/17/investing-in-space-a-guide-to-satellites.html" >🔗</a> **[CNBC]** Investing in Space: A guide to satellites


- <a href="https://www.cnbc.com/2023/08/17/bae-buys-ball-aerospace-for-5point6-billion.html" >🔗</a> **[CNBC]** UK defense contractor BAE buying Ball’s aerospace division for $5.6 billion


- <a href="https://spacenews.com/northrop-grumman-to-get-sole-source-contract-for-space-force-radar-sites/" >🔗</a> **[SpaceNews]** Northrop Grumman to get sole-source contract for Space Force radar sites


- <a href="https://spacenews.com/bae-systems-to-acquire-ball-aerospace-for-5-5-billion/" >🔗</a> **[SpaceNews]** BAE Systems to acquire Ball Aerospace for $5.5 billion


- <a href="https://spacenews.com/terran-orbital-orbital-expects-180-million-payment-from-rivada-space-this-year/" >🔗</a> **[SpaceNews]** Terran Orbital expects $180 million payment from Rivada Space this year


- <a href="https://spacepolicyonline.com/news/state-department-kicks-off-international-lunar-year-discussions/" >🔗</a> **[SpacePolicyOnline.com]** State Department Kicks Off International Lunar Year Discussions


- <a href="http://www.nasa.gov/press-release/nasa-s-spacex-crew-6-to-discuss-space-station-mission-upcoming-return" >🔗</a> **[NASA]** NASA’s SpaceX Crew-6 to Discuss Space Station Mission, Upcoming Return


  - <a href="https://go4liftoff.com/launch/id/bc325945-4bee-4412-84e1-14998b2eba5f" >🚀</a> **Falcon 9 Block 5 | Crew-6** from Kennedy Space Center, FL, USA




  - <a href="https://go4liftoff.com/event/id/772" >📆</a> **SpaceX Crew-6 Crew Dragon Splashdown**

  - <a href="https://go4liftoff.com/event/id/771" >📆</a> **SpaceX Crew-6 Crew Dragon Undocking**


- <a href="http://www.nasa.gov/press-release/nasa-hosts-astronaut-loral-o-hara-s-prelaunch-interviews" >🔗</a> **[NASA]** NASA Hosts Astronaut Loral O’Hara’s Prelaunch Interviews


  - <a href="https://go4liftoff.com/launch/id/2a052554-35be-4e6c-8d60-b2b9072de17c" >🚀</a> **Soyuz 2.1a | Soyuz MS-24** from Baikonur Cosmodrome, Republic of Kazakhstan



- <a href="https://www.nasaspaceflight.com/2023/08/launch-roundup-081623/" >🔗</a> **[NASASpaceflight]** Launch Roundup: three back-to-back Starlink missions to cross 5,000 Starlink satellites launched


  - <a href="https://go4liftoff.com/launch/id/09642682-60f3-4470-a802-18788601c5a5" >🚀</a> **Falcon 9 Block 5 | Starlink Group 6-10** from Cape Canaveral, FL, USA

  - <a href="https://go4liftoff.com/launch/id/15699687-3fb1-4749-9680-fc858e5e7081" >🚀</a> **Falcon 9 Block 5 | Starlink Group 7-1** from Vandenberg SFB, CA, USA

  - <a href="https://go4liftoff.com/launch/id/87fba73c-f085-4abf-830d-fae92c599977" >🚀</a> **Falcon 9 Block 5 | Starlink Group 6-11** from Cape Canaveral, FL, USA



- <a href="https://spacenews.com/momentus-cuts-workforce-while-evaluating-strategic-options/" >🔗</a> **[SpaceNews]** Momentus cuts workforce while evaluating strategic options




## Latest Blog Posts 🪧

- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-august-7-13-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: August 7-13, 2023


- <a href="https://www.planetary.org/the-downlink/hasta-la-vista-baby" >🔗</a> **[Planetary Society]** Hasta la vista, baby


- <a href="https://blog.ulalaunch.com/blog/icps-3-upperstage-that-will-propel-artemis-iii-astronauts-to-the-moon-arrives-for-processing" >🔗</a> **[United Launch Alliance]** ICPS-3: Upperstage that will propel Artemis III astronauts to the Moon arrives for processing


- <a href="https://www.planetary.org/articles/exoplanet-terminator-zones-search-for-life" >🔗</a> **[Planetary Society]** Are exoplanet 'terminator zones' a lead in the search for life?


- <a href="https://blog.ulalaunch.com/blog/icps-2-orion-will-observe-upper-stage-after-launch" >🔗</a> **[United Launch Alliance]** ICPS-2: Rendezvous target guides Artemis II Orion demonstrations


  - <a href="https://go4liftoff.com/launch/id/41699701-2ef4-4b0c-ac9d-6757820cde87" >🚀</a> **SLS Block 1 | Artemis II** from Kennedy Space Center, FL, USA



- <a href="https://europeanspaceflight.substack.com/p/to-stream-or-not-to-stream" >🔗</a> **[European Spaceflight]** To stream or not to stream


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-july-24-august-6-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: July 24-August 6, 2023


- <a href="https://www.planetary.org/the-downlink/far-out-man" >🔗</a> **[Planetary Society]** Far out, man!


- <a href="https://blog.ulalaunch.com/blog/silentbarker-atlas-v-stacked-for-national-security-launch" >🔗</a> **[United Launch Alliance]** SILENTBARKER/NROL-107: Atlas V stacked for national security launch


- <a href="https://europeanspaceflight.substack.com/p/will-esa-finally-land-on-mars" >🔗</a> **[European Spaceflight]** Will ESA finally land on Mars?




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230817T181703">2023-08-17 18:17:03 UTC</a>
  <br>
</div>