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
- <a href="https://spacenews.com/spaced-ventures-first-exit-sidus-space-purchase-of-exo-space/" >🔗</a> **[SpaceNews]** Spaced Ventures’ first exit: Sidus Space purchase of Exo-Space


- <a href="https://spacenews.com/chandrayaan-3-india-becomes-fourth-country-to-land-on-the-moon/" >🔗</a> **[SpaceNews]** Chandrayaan-3: India becomes fourth country to land on the moon


  - <a href="https://go4liftoff.com/launch/id/78f7c31d-4f29-482a-96d1-390b460a0a02" >🚀</a> **LVM-3 | Chandrayaan-3** from Satish Dhawan Space Centre, India



- <a href="https://www.cnbc.com/2023/08/23/india-chandrayaan-3-moon-mission.html" >🔗</a> **[CNBC]** India becomes fourth country to land on the moon, first on south pole, with Chandrayaan-3 spacecraft


  - <a href="https://go4liftoff.com/launch/id/78f7c31d-4f29-482a-96d1-390b460a0a02" >🚀</a> **LVM-3 | Chandrayaan-3** from Satish Dhawan Space Centre, India




  - <a href="https://go4liftoff.com/event/id/780" >📆</a> **Chandrayaan-3 Lunar Landing**


- <a href="https://spacenews.com/target-of-european-debris-removal-mission-hit-by-other-debris/" >🔗</a> **[SpaceNews]** Target of European debris removal mission hit by other debris


  - <a href="https://go4liftoff.com/launch/id/351bea09-3fcf-4195-8c97-adeeaf9708ea" >🚀</a> **Vega | Proba-V, VNREDSat 1A, ESTCube-1** from Kourou, French Guiana

  - <a href="https://go4liftoff.com/launch/id/b0634bea-4769-4846-8546-b7574d571bbc" >🚀</a> **Vega-C | ClearSpace-1** from Kourou, French Guiana



- <a href="https://www.teslarati.com/nasa-spacex-give-go-crew-7-launch/" >🔗</a> **[Teslarati]** NASA and SpaceX give GO for Crew 7 launch


  - <a href="https://go4liftoff.com/launch/id/1caacff9-837e-493b-afd4-4da54eeccdf2" >🚀</a> **Falcon 9 Block 5 | Crew-7** from Kennedy Space Center, FL, USA



- <a href="https://arstechnica.com/space/2023/08/police-are-investigating-an-indian-actor-for-joking-about-the-countrys-moon-lander/" >🔗</a> **[Arstechnica]** Police are investigating an Indian actor for joking about the country’s Moon lander


- <a href="https://spacenews.com/polaris-dawn-mission-likely-to-slip-to-2024/" >🔗</a> **[SpaceNews]** Polaris Dawn mission likely to slip to 2024


  - <a href="https://go4liftoff.com/launch/id/b69cfada-3320-4331-89e1-aaa8b49e6a9c" >🚀</a> **Falcon 9 Block 5 | Polaris Dawn** from Kennedy Space Center, FL, USA



- <a href="https://spacenews.com/mynaric-to-design-optical-ground-terminal-for-u-s-military-constellation/" >🔗</a> **[SpaceNews]** Mynaric to design optical ground terminal for U.S. military constellation


- <a href="https://www.teslarati.com/spacex-launches-100th-dedicated-starlink-mission/" >🔗</a> **[Teslarati]** SpaceX launches 100th dedicated Starlink mission


  - <a href="https://go4liftoff.com/launch/id/15699687-3fb1-4749-9680-fc858e5e7081" >🚀</a> **Falcon 9 Block 5 | Starlink Group 7-1** from Vandenberg SFB, CA, USA



- <a href="https://spacenews.com/u-s-intelligence-office-to-investigate-lagging-procurement-of-commercial-satellite-data/" >🔗</a> **[SpaceNews]** U.S. intelligence office to investigate lagging procurement of commercial satellite data




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/articles/total-solar-eclipse-2024-path-of-totality" >🔗</a> **[Planetary Society]** Total solar eclipse 2024: Why it’s worth getting into the path of totality


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-august-14-20-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: August 14-20, 2023


- <a href="https://europeanspaceflight.substack.com/p/whats-going-on-with-saxavord-contractors" >🔗</a> **[European Spaceflight]** What’s going on with SaxaVord contractors?


- <a href="https://www.planetary.org/the-downlink/storms-and-showers" >🔗</a> **[Planetary Society]** Storms and showers


- <a href="https://blog.ulalaunch.com/blog/silentbarker/nrol-107-countdown-rehearsal-tests-atlas-v" >🔗</a> **[United Launch Alliance]** SILENTBARKER/NROL-107: Countdown rehearsal tests Atlas V rocket


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-august-7-13-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: August 7-13, 2023


- <a href="https://blog.ulalaunch.com/blog/icps-3-upperstage-that-will-propel-artemis-iii-astronauts-to-the-moon-arrives-for-processing" >🔗</a> **[United Launch Alliance]** ICPS-3: Upper stage that will propel Artemis III astronauts to the Moon arrives for processing


- <a href="https://www.planetary.org/the-downlink/hasta-la-vista-baby" >🔗</a> **[Planetary Society]** Hasta la vista, baby


- <a href="https://www.planetary.org/articles/exoplanet-terminator-zones-search-for-life" >🔗</a> **[Planetary Society]** Are exoplanet 'terminator zones' a lead in the search for life?


- <a href="https://blog.ulalaunch.com/blog/icps-2-orion-will-observe-upper-stage-after-launch" >🔗</a> **[United Launch Alliance]** ICPS-2: Rendezvous target guides Artemis II Orion demonstrations


  - <a href="https://go4liftoff.com/launch/id/41699701-2ef4-4b0c-ac9d-6757820cde87" >🚀</a> **SLS Block 1 | Artemis II** from Kennedy Space Center, FL, USA





<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230823T131619">2023-08-23 13:16:19 UTC</a>
  <br>
</div>