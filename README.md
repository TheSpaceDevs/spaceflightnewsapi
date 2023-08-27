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
- <a href="https://www.nasaspaceflight.com/2023/08/space-rider-update/" >🔗</a> **[NASASpaceflight]** ESA’s Space Rider likely to launch third quarter of 2025, program manager says


  - <a href="https://go4liftoff.com/launch/id/d74f2e7b-a8b7-4d8f-8ecd-193e73937664" >🚀</a> **Vega-C | Space Rider** from Kourou, French Guiana



- <a href="https://tlpnetwork.com/news/2023/08/australian-space-imagery-startup-heo-raises-8-million" >🔗</a> **[The Launch Pad]** Australian Space Imagery Startup HEO Raises $8 Million


- <a href="https://tlpnetwork.com/news/2023/08/sedaro-secures-us-space-force-contract-to-develop-digital-spacecraft-twins" >🔗</a> **[The Launch Pad]** Sedaro Secures US Space Force Contract To Develop Digital Spacecraft Twins


- <a href="https://spacenews.com/crew-7-launches-to-the-space-station/" >🔗</a> **[SpaceNews]** Crew-7 launches to the space station


  - <a href="https://go4liftoff.com/launch/id/1caacff9-837e-493b-afd4-4da54eeccdf2" >🚀</a> **Falcon 9 Block 5 | Crew-7** from Kennedy Space Center, FL, USA



- <a href="https://spacepolicyonline.com/news/international-crew-on-its-way-to-iss/" >🔗</a> **[SpacePolicyOnline.com]** International Crew On Its Way to ISS


  - <a href="https://go4liftoff.com/launch/id/1caacff9-837e-493b-afd4-4da54eeccdf2" >🚀</a> **Falcon 9 Block 5 | Crew-7** from Kennedy Space Center, FL, USA



- <a href="http://www.nasa.gov/press-release/nasa-s-spacex-crew-7-launches-to-international-space-station" >🔗</a> **[NASA]** NASA’s SpaceX Crew-7 Launches to International Space Station


  - <a href="https://go4liftoff.com/launch/id/1caacff9-837e-493b-afd4-4da54eeccdf2" >🚀</a> **Falcon 9 Block 5 | Crew-7** from Kennedy Space Center, FL, USA



- <a href="https://www.cnbc.com/2023/08/26/spacex-launches-crew-7-astronaut-mission-for-nasa.html" >🔗</a> **[CNBC]** SpaceX launches Crew-7 mission, the company’s 11th carrying astronauts


  - <a href="https://go4liftoff.com/launch/id/1caacff9-837e-493b-afd4-4da54eeccdf2" >🚀</a> **Falcon 9 Block 5 | Crew-7** from Kennedy Space Center, FL, USA



- <a href="https://tlpnetwork.com/news/2023/08/second-viasat-suffers-anomaly-in-orbit" >🔗</a> **[The Launch Pad]** 2nd ViaSat Suffers Anomaly In Orbit


  - <a href="https://go4liftoff.com/launch/id/d6e60f3b-21d0-44f9-be02-fe0c00289b6a" >🚀</a> **Falcon 9 Block 5 | Inmarsat-6 F2** from Cape Canaveral, FL, USA



- <a href="https://tlpnetwork.com/news/2023/08/oneweb-eutelsat-merger-hinges-on-shareholder-vote" >🔗</a> **[The Launch Pad]** OneWeb-Eutelsat Merger Hinges on Shareholder Vote


- <a href="https://tlpnetwork.com/news/2023/08/27-european-union-states-pledge-to-avoid-destructive-anti-satellite-tests" >🔗</a> **[The Launch Pad]** 27 European Union States Pledge to Avoid Destructive Anti-Satellite Tests




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
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230827T111006">2023-08-27 11:10:06 UTC</a>
  <br>
</div>