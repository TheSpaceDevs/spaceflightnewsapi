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
- <a href="https://europeanspaceflight.com/polaris-spaceplanes-begins-testing-its-mira-light-vehicle/" >🔗</a> **[European Spaceflight]** POLARIS Spaceplanes Begins Testing its MIRA-Light Vehicle


- <a href="https://spacenews.com/rideshare-industry-adapting-to-a-changing-smallsat-market/" >🔗</a> **[SpaceNews]** Rideshare industry adapting to a changing smallsat market


- <a href="https://spacenews.com/big-constellations-no-longer-necessarily-mean-small-satellites/" >🔗</a> **[SpaceNews]** Big constellations no longer necessarily mean small satellites


- <a href="https://spacenews.com/defense-innovation-unit-to-sponsor-a-rapid-response-space-mission/" >🔗</a> **[SpaceNews]** Defense Innovation Unit to sponsor a rapid response space mission


- <a href="https://spacenews.com/can-space-investment-become-cool-again/" >🔗</a> **[SpaceNews]** Can space investment become cool again?


- <a href="https://spacenews.com/european-union-nations-join-asat-testing-ban/" >🔗</a> **[SpaceNews]** European Union nations join ASAT testing ban


- <a href="https://tlpnetwork.com/news/2023/08/rocketlab-flys-recovered-electron-engine-for-first-time" >🔗</a> **[The Launch Pad]** RocketLab Flys Recovered Electron Engine For First Time


  - <a href="https://go4liftoff.com/launch/id/7975274c-81c5-48a5-82e1-9b8d982cd533" >🚀</a> **Electron | We Love the Nightlife (Capella Acadia 1)** from Onenui Station, Mahia Peninsula, New Zealand



- <a href="https://spacenews.com/space-force-to-seek-industry-ideas-for-rapid-deployment-of-satellites/" >🔗</a> **[SpaceNews]** Space Force to seek industry ideas for rapid deployment of satellites


- <a href="https://www.cnbc.com/2023/08/24/viasats-inmarsat-i6-f2-satellite-suffers-power-failure.html" >🔗</a> **[CNBC]** Viasat reports second satellite malfunction in a matter of weeks


  - <a href="https://go4liftoff.com/launch/id/d6e60f3b-21d0-44f9-be02-fe0c00289b6a" >🚀</a> **Falcon 9 Block 5 | Inmarsat-6 F2** from Cape Canaveral, FL, USA



- <a href="https://tlpnetwork.com/news/2023/08/north-korea-fails-to-launch-spy-satellite-again" >🔗</a> **[The Launch Pad]** North Korea Fails To Launch Spy Satellite Again


  - <a href="https://go4liftoff.com/launch/id/b3950eeb-e69a-465a-8c73-78dd2180028c" >🚀</a> **Chollima-1 | Malligyong-1b** from Sohae Satellite Launching Station,  Cholsan County, North Pyongan Province, Democratic People's Republic of Korea





## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/the-downlink/moonstruck" >🔗</a> **[Planetary Society]** Moonstruck


- <a href="https://blog.ulalaunch.com/blog/rocketstars-engineer-moves-from-aircraft-to-launching-satellites-at-ula" >🔗</a> **[United Launch Alliance]** RocketStars: Engineer moves from aircraft to launching satellites at ULA


- <a href="https://www.planetary.org/articles/what-would-happen-if-an-asteroid-hit-the-moon" >🔗</a> **[Planetary Society]** What would happen if an asteroid hit the Moon?


- <a href="https://blog.ulalaunch.com/blog/silentbarker/nrol-107-payload-mate-mounted-to-atlas-v-for-launch" >🔗</a> **[United Launch Alliance]** SILENTBARKER/NROL-107: Payload mounted to Atlas V for launch


- <a href="https://www.planetary.org/articles/total-solar-eclipse-2024-path-of-totality" >🔗</a> **[Planetary Society]** Total solar eclipse 2024: Why it’s worth getting into the path of totality


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-august-14-20-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: August 14-20, 2023


- <a href="https://europeanspaceflight.substack.com/p/whats-going-on-with-saxavord-contractors" >🔗</a> **[European Spaceflight]** What’s going on with SaxaVord contractors?


- <a href="https://www.planetary.org/the-downlink/storms-and-showers" >🔗</a> **[Planetary Society]** Storms and showers


- <a href="https://blog.ulalaunch.com/blog/silentbarker/nrol-107-countdown-rehearsal-tests-atlas-v" >🔗</a> **[United Launch Alliance]** SILENTBARKER/NROL-107: Countdown rehearsal tests Atlas V rocket


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-august-7-13-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: August 7-13, 2023




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230825T151344">2023-08-25 15:13:44 UTC</a>
  <br>
</div>