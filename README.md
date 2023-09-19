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
- <a href="https://spacenews.com/electron-fails-during-capella-space-launch/" >🔗</a> **[SpaceNews]** Electron fails during Capella Space launch


  - <a href="https://go4liftoff.com/launch/id/08f52ca7-9aba-41d1-a5c7-092cab7aca92" >🚀</a> **Electron | We Will Never Desert You (Capella Acadia 2)** from Onenui Station, Mahia Peninsula, New Zealand



- <a href="https://tlpnetwork.com/news/2023/09/rocketlab-41-electron-mission-launch-failure" >🔗</a> **[The Launch Pad]** DEVELOPING STORY: RocketLab Electron Launch Failure


  - <a href="https://go4liftoff.com/launch/id/08f52ca7-9aba-41d1-a5c7-092cab7aca92" >🚀</a> **Electron | We Will Never Desert You (Capella Acadia 2)** from Onenui Station, Mahia Peninsula, New Zealand



- <a href="https://arstechnica.com/culture/2023/09/a-water-carrier-just-won-the-hardest-cycling-race-on-the-planet/" >🔗</a> **[Arstechnica]** A water carrier just won the hardest cycling race on the planet


- <a href="http://www.nasa.gov/press-release/nasa-finalizes-coverage-for-first-us-asteroid-sample-landing" >🔗</a> **[NASA]** NASA Finalizes Coverage for First US Asteroid Sample Landing


  - <a href="https://go4liftoff.com/launch/id/0bcc6850-4c51-4b08-aa19-0b3753351b9b" >🚀</a> **Atlas V 411 | OSIRIS-REx** from Cape Canaveral, FL, USA




  - <a href="https://go4liftoff.com/event/id/36" >📆</a> **OSIRIS-Rex Sample Return**


- <a href="https://spacenews.com/abl-gets-contract-for-u-s-space-force-responsive-launch-mission/" >🔗</a> **[SpaceNews]** ABL gets contract for U.S. Space Force ‘responsive launch’ mission


- <a href="https://www.nasaspaceflight.com/2023/09/launch-roundup-091823/" >🔗</a> **[NASASpaceflight]** Launch Roundup; Rocket Lab fails during “We Will Never Desert You” launch; SpaceX to launch booster for 17th time


  - <a href="https://go4liftoff.com/launch/id/08f52ca7-9aba-41d1-a5c7-092cab7aca92" >🚀</a> **Electron | We Will Never Desert You (Capella Acadia 2)** from Onenui Station, Mahia Peninsula, New Zealand

  - <a href="https://go4liftoff.com/launch/id/7fc31961-b46f-4a45-9b1d-3caece884f61" >🚀</a> **Falcon 9 Block 5 | Starlink Group 6-17** from Cape Canaveral, FL, USA

  - <a href="https://go4liftoff.com/launch/id/1c099ba2-9b8f-4364-8ba0-0c26f7993dd5" >🚀</a> **Falcon 9 Block 5 | Starlink Group 6-18** from Cape Canaveral, FL, USA



- <a href="https://tlpnetwork.com/news/2023/09/abl-secures-15-million-space-system-command-responsive-launch-contract" >🔗</a> **[The Launch Pad]** ABL Secures $15 Million Space System Command Responsive Launch Contract


- <a href="https://mars.nasa.gov/news/9480/" >🔗</a> **[NASA]** NASA's Curiosity Reaches Mars Ridge Where Water Left Debris Pileup


  - <a href="https://go4liftoff.com/launch/id/df8d4fdb-9add-4ce9-9f0e-aae1c61df212" >🚀</a> **Atlas V 541 | MSL (Curiosity)** from Cape Canaveral, FL, USA



- <a href="https://spacenews.com/china-launches-new-batch-of-yaogan-reconnaissance-satellites/" >🔗</a> **[SpaceNews]** China launches new batch of Yaogan reconnaissance satellites


  - <a href="https://go4liftoff.com/launch/id/1c09bb7e-5d7c-4ca7-a4a8-81db7004c66f" >🚀</a> **Long March 2D | Yaogan 39 Group 02** from Xichang Satellite Launch Center, People's Republic of China



- <a href="https://spacenews.com/l3harris-exploring-supplier-partnerships-for-its-satellite-business/" >🔗</a> **[SpaceNews]** L3Harris exploring supplier partnerships for its satellite business




## Latest Blog Posts 🪧

- <a href="https://europeanspaceflight.substack.com/p/is-there-a-future-for-the-european" >🔗</a> **[European Spaceflight]** Is there a future for the European Astronaut Corps?


- <a href="https://www.planetary.org/the-downlink/lost-and-found" >🔗</a> **[Planetary Society]** Lost and found


- <a href="https://www.planetary.org/articles/guide-to-eclipse-vocabulary" >🔗</a> **[Planetary Society]** A guide to eclipse vocabulary


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-september-4-10-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: September 4-10, 2023


- <a href="https://www.planetary.org/the-downlink/cometary-sights-and-sounds" >🔗</a> **[Planetary Society]** Cometary sights and sounds


- <a href="https://www.planetary.org/articles/eclipse-2024-checklist" >🔗</a> **[Planetary Society]** A checklist for what to expect during the 2024 total solar eclipse


- <a href="https://www.planetary.org/articles/are-your-solar-eclipse-glasses-safe" >🔗</a> **[Planetary Society]** Are your solar eclipse glasses safe?


- <a href="https://www.planetary.org/articles/how-to-see-newly-discovered-comet-nishimura" >🔗</a> **[Planetary Society]** How to see newly discovered Comet Nishimura


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-august-28-september-3-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: August 28-September 3, 2023


- <a href="https://www.planetary.org/articles/osiris-rex-sample-return-what-to-expect" >🔗</a> **[Planetary Society]** OSIRIS-REx sample return: What to expect




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230919T111141">2023-09-19 11:11:41 UTC</a>
  <br>
</div>