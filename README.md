![Cover](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/profile/assets/snapi_poster.png)

[![Website](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/profile/assets/badge_snapi_website.svg)](https://spaceflightnewsapi.net/)
[![Documentation](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/profile/assets/badge_snapi_doc.svg)](https://api.spaceflightnewsapi.net/v4/docs)
[![Version](https://img.shields.io/github/v/release/TheSpaceDevs/spaceflightnewsapi?style=for-the-badge)](https://github.com/TheSpaceDevs/spaceflightnewsapi/releases/tag/v4.0.1)
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

- TechCrunch
- SpaceFlight Insider
- SpaceX
- ElonX
- Blue Origin
- Spaceflight Now
- Space.com
- Teslarati
- Virgin Galactic
- Planetary Society
- Phys
- National Space Society
- The Japan Times
- National Geographic
- SpaceNews
- The National
- Jet Propulsion Laboratory
- NASA
- The Space Review
- The Verge
- The Drive
- Arstechnica
- ESA
- The Space Devs
- AmericaSpace
- The Wall Street Journal
- CNBC
- United Launch Alliance
- Reuters
- The New York Times
- euronews
- European Spaceflight Update
- NASASpaceflight
- SyFy
- The Launch Pad


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



## Latest News Articles ⌛
- <a href="https://spacenews.com/agencies-studying-safety-issues-of-lox-methane-launch-vehicles/" >🔗</a> **[SpaceNews]** Agencies studying safety issues of LOX/methane launch vehicles


- <a href="https://www.nasaspaceflight.com/2023/05/perseverance-mars-express-update/" >🔗</a> **[NASASpaceflight]** Perseverance finds Mars river could have been ‘wilder,’ Mars Express takes new volcano images


  - <a href="https://go4liftoff.com/launch/id/db62cfa1-4d10-41d3-b25f-a58e138ce202" >🚀</a> **Soyuz-FG | Mars Express** from Baikonur Cosmodrome, Republic of Kazakhstan

  - <a href="https://go4liftoff.com/launch/id/c4db6995-f25f-4608-8eb9-ce95d5226af2" >🚀</a> **Atlas V 541 | Mars 2020 (Perseverance rover & Ingenuity helicopter)** from Cape Canaveral, FL, USA



- <a href="https://spacenews.com/spacex-launches-oneweb-gen-2-technology-demonstrator/" >🔗</a> **[SpaceNews]** SpaceX launches OneWeb Gen 2 technology demonstrator


  - <a href="https://go4liftoff.com/launch/id/6d55d3cf-5c95-4c23-8c5e-1da44fbe299d" >🚀</a> **Falcon 9 Block 5 | Iridium-9 & OneWeb 19** from Vandenberg SFB, CA, USA



- <a href="https://www.teslarati.com/nasa-selects-blue-origin-to-land-astronauts-on-the-moon/" >🔗</a> **[Teslarati]** NASA selects Blue Origin to land Astronauts on the Moon


  - <a href="https://go4liftoff.com/launch/id/d7042e81-6420-449d-8154-2611641e9822" >🚀</a> **SLS Block 1B | Artemis V** from Kennedy Space Center, FL, USA




  - <a href="https://go4liftoff.com/event/id/778" >📆</a> **NASA Artemis V Lander Announcement**


- <a href="https://www.nasaspaceflight.com/2023/05/twis2023-05-19/" >🔗</a> **[NASASpaceflight]** This Week In Spaceflight: SpaceX’s Raptor breaks records, NASA announces second Artemis Lander


  - <a href="https://go4liftoff.com/launch/id/d7042e81-6420-449d-8154-2611641e9822" >🚀</a> **SLS Block 1B | Artemis V** from Kennedy Space Center, FL, USA




  - <a href="https://go4liftoff.com/event/id/778" >📆</a> **NASA Artemis V Lander Announcement**


- <a href="http://www.nasa.gov/press-release/nasa-extends-nancy-grace-roman-space-telescope-science-operations" >🔗</a> **[NASA]** NASA Extends Nancy Grace Roman Space Telescope Science Operations


  - <a href="https://go4liftoff.com/launch/id/521f3a1c-f977-4306-9b7f-495858719adf" >🚀</a> **Falcon Heavy | Nancy Grace Roman Space Telescope** from Kennedy Space Center, FL, USA



- <a href="https://spacenews.com/technical-strengths-and-lower-cost-led-nasa-to-select-blue-origin-lander/" >🔗</a> **[SpaceNews]** Technical strengths and lower cost led NASA to select Blue Origin lander


  - <a href="https://go4liftoff.com/launch/id/d7042e81-6420-449d-8154-2611641e9822" >🚀</a> **SLS Block 1B | Artemis V** from Kennedy Space Center, FL, USA




  - <a href="https://go4liftoff.com/event/id/778" >📆</a> **NASA Artemis V Lander Announcement**


- <a href="https://spacenews.com/hasc-chairman-questions-continued-delays-in-settling-dispute-over-space-commands-location/" >🔗</a> **[SpaceNews]** HASC chairman questions ‘continued delays’ in settling dispute over Space Command’s location


- <a href="https://www.teslarati.com/spacex-launches-22-v2-mini-starlink-satellites/" >🔗</a> **[Teslarati]** SpaceX launches 22 V2 mini Starlink satellites


  - <a href="https://go4liftoff.com/launch/id/0962fe02-4a3d-4131-8bc5-ee7bd2bc97fa" >🚀</a> **Falcon 9 Block 5 | Starlink Group 6-3** from Cape Canaveral, FL, USA



- <a href="http://www.nasa.gov/press-release/nasa-selects-winners-announces-final-phase-of-space-food-challenge" >🔗</a> **[NASA]** NASA Selects Winners, Announces Final Phase of Space Food Challenge




## Latest Blog Posts 🚀

- <a href="https://www.planetary.org/the-downlink/moon-spying-missions-and-a-planetary-evil-twin" >🔗</a> **[Planetary Society]** Moon-spying missions and a planetary evil twin


- <a href="https://blog.ulalaunch.com/blog/hypersonic-missiles-are-just-misunderstood" >🔗</a> **[United Launch Alliance]** Hypersonic Missiles are Just Misunderstood


- <a href="https://www.planetary.org/articles/why-is-venus-called-earths-twin" >🔗</a> **[Planetary Society]** Why is Venus called Earth’s twin?


- <a href="https://www.planetary.org/the-downlink/hard-working-spacecraft-and-even-harder-working-microbes" >🔗</a> **[Planetary Society]** Hard-working spacecraft and even harder-working microbes


- <a href="https://www.planetary.org/articles/why-has-spacexs-starship-sparked-an-environmental-controversy" >🔗</a> **[Planetary Society]** Why has SpaceX's Starship sparked an environmental controversy?


- <a href="https://www.planetary.org/articles/how-did-earth-get-its-oxygen" >🔗</a> **[Planetary Society]** How did Earth get its oxygen?


- <a href="https://www.planetary.org/careers/freelance-digital-advertising-specialist-contract-part-time" >🔗</a> **[Planetary Society]** Freelance Digital Advertising Specialist (Contract & Part-time)


- <a href="https://www.planetary.org/the-downlink/moonshadow-moonshadow" >🔗</a> **[Planetary Society]** Moonshadow, Moonshadow


- <a href="https://blog.ulalaunch.com/blog/why-is-stem-education-a-national-imperative" >🔗</a> **[United Launch Alliance]** Why is STEM Education a National Imperative and How Are We Wasting Our Precious Human Resource?


- <a href="https://www.planetary.org/articles/what-happened-with-psyche" >🔗</a> **[Planetary Society]** What happened with Psyche?




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230521T113041">2023-05-21 11:30:41 UTC</a>
  <br>
</div>