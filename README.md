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
- <a href="https://tlpnetwork.com/news/2023/08/nasa-esa-csa-jaxa-commit-to-iss-operations-through-2030" >🔗</a> **[The Launch Pad]** NASA, ESA, CSA, and JAXA Commit To ISS Operations Through 2030


- <a href="https://tlpnetwork.com/news/2023/08/isro-chandrayaan-3-lunar-orbit-confirmed" >🔗</a> **[The Launch Pad]** ISRO Chandrayaan-3 Lunar Orbit Confirmed


- <a href="https://spacenews.com/indias-chandrayaan-3-lander-arrives-in-lunar-orbit/" >🔗</a> **[SpaceNews]** India’s Chandrayaan-3 lander arrives in lunar orbit


- <a href="https://spacenews.com/astra-lays-off-reassigns-employees-as-it-refocuses-on-satellite-propulsion/" >🔗</a> **[SpaceNews]** Astra lays off, reassigns employees as it refocuses on satellite propulsion


- <a href="https://arstechnica.com/space/2023/08/a-look-at-the-surprising-history-of-the-earliest-rocket-pioneers/" >🔗</a> **[Arstechnica]** A look at the surprising history of the earliest rocket pioneers


- <a href="https://spacenews.com/apple-backed-globalstars-revenue-jump-underlines-iot-opportunity/" >🔗</a> **[SpaceNews]** Apple-backed Globalstar’s revenue jump underlines IoT opportunity


- <a href="https://www.cnbc.com/2023/08/04/astra-conducts-layoffs-raises-debt-shifts-focus-to-spacecraft-engines.html" >🔗</a> **[CNBC]** Astra conducts layoffs, raises debt and shifts focus to spacecraft engines in bid to survive


- <a href="https://www.teslarati.com/spacex-performs-booster-9-engine-test-ahead-of-static-fire/" >🔗</a> **[Teslarati]** SpaceX performs Booster 9 engine test ahead of static fire


  - <a href="https://go4liftoff.com/launch/id/04b91bb8-38a7-4868-b025-4bbe05d1fbfe" >🚀</a> **Starship | Integrated Flight Test 2** from SpaceX Space Launch Facility, TX, USA




  - <a href="https://go4liftoff.com/event/id/844" >📆</a> **Booster 9 Testing**

  - <a href="https://go4liftoff.com/event/id/845" >📆</a> **Booster 9 33 Engines Static Fire**


- <a href="https://arstechnica.com/space/2023/08/voyager-2-phones-home-and-says-everything-is-cool/" >🔗</a> **[Arstechnica]** Voyager 2 phones home and says everything is cool


  - <a href="https://go4liftoff.com/launch/id/75414835-ec0a-43f4-b624-1636502312f3" >🚀</a> **Titan IIIE | Voyager 2** from Cape Canaveral, FL, USA



- <a href="https://www.nasaspaceflight.com/2023/08/china-roundup-080423/" >🔗</a> **[NASASpaceflight]** China launches four rockets and outlines future lunar mission


  - <a href="https://go4liftoff.com/launch/id/160d6bd1-4ac6-43bd-8284-12e457cde9d7" >🚀</a> **Ceres-1 | Qiankun-1 & Xingshidai‐16** from Jiuquan Satellite Launch Center, People's Republic of China

  - <a href="https://go4liftoff.com/launch/id/22a6f1ed-afcd-455d-9316-5aaf8f39e864" >🚀</a> **Long March 2D | Skysight AS-01 to 03 & Lingxi-03** from Taiyuan Satellite Launch Center, People's Republic of China

  - <a href="https://go4liftoff.com/launch/id/9da1b09b-d448-43a2-b6f1-720756c4e960" >🚀</a> **Long March 2D | Yaogan 36 Group 05** from Xichang Satellite Launch Center, People's Republic of China

  - <a href="https://go4liftoff.com/launch/id/5749ccdb-a743-49e9-b7d0-3c018dc68ae3" >🚀</a> **Long March 4C | Fengyun-3F** from Jiuquan Satellite Launch Center, People's Republic of China





## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/the-downlink/far-out-man" >🔗</a> **[Planetary Society]** Far out, man!


- <a href="https://blog.ulalaunch.com/blog/silentbarker-atlas-v-stacked-for-national-security-launch" >🔗</a> **[United Launch Alliance]** SILENTBARKER/NROL-107: Atlas V stacked for national security launch


- <a href="https://europeanspaceflight.substack.com/p/will-esa-finally-land-on-mars" >🔗</a> **[European Spaceflight]** Will ESA finally land on Mars?


- <a href="https://www.planetary.org/mission-control" >🔗</a> **[Planetary Society]** LightSail 2 Mission Control


- <a href="https://www.planetary.org/the-downlink/aquatic-equivalencies" >🔗</a> **[Planetary Society]** Aquatic equivalencies


- <a href="https://www.planetary.org/articles/life-on-venus-your-questions-answered" >🔗</a> **[Planetary Society]** Life on Venus: Your Questions Answered


- <a href="https://europeanspaceflight.substack.com/p/the-time-europe-tried-to-copy-energia" >🔗</a> **[European Spaceflight]** The time Europe tried to copy Energia


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-july-17-23-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: July 17-23, 2023


- <a href="https://europeanspaceflight.substack.com/p/how-can-thales-use-space-rider-ip" >🔗</a> **[European Spaceflight]** How can Thales use Space Rider IP for Rev-1?


- <a href="https://www.planetary.org/the-downlink/thats-a-mare" >🔗</a> **[Planetary Society]** That’s a mare




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230805T181517">2023-08-05 18:15:17 UTC</a>
  <br>
</div>