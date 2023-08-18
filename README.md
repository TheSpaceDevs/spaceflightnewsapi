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
- <a href="https://europeanspaceflight.com/polaris-to-begin-testing-fourth-spaceplane-demonstrator-from-september/" >🔗</a> **[European Spaceflight]** POLARIS to Begin Testing Fourth Spaceplane Demonstrator From September


- <a href="https://spacenews.com/u-s-government-warns-of-foreign-intelligence-threats-to-the-space-industry/" >🔗</a> **[SpaceNews]** U.S. government warns of foreign intelligence threats to the space industry


- <a href="https://spacenews.com/poland-signs-agreement-to-fly-astronaut-on-axiom-space-iss-mission/" >🔗</a> **[SpaceNews]** Poland signs agreement to fly astronaut on Axiom Space ISS mission


- <a href="https://arstechnica.com/space/2023/08/rocket-report-europes-final-countdown-for-2023-sls-to-carry-more-cubesats/" >🔗</a> **[Arstechnica]** Rocket Report: Russian rocket lands like an airplane; SpaceX steamroller rolls


- <a href="https://spacenews.com/japanese-sar-company-iqps-to-launch-with-rocket-lab-after-virgin-orbit-bankruptcy/" >🔗</a> **[SpaceNews]** Japanese SAR company iQPS to launch with Rocket Lab after Virgin Orbit bankruptcy


  - <a href="https://go4liftoff.com/launch/id/2918b5f6-1340-4c73-bb75-4f9b5e16999f" >🚀</a> **Electron | The Moon God Awakens (QPS-SAR-5)** from Onenui Station, Mahia Peninsula, New Zealand



- <a href="http://www.nasa.gov/press-release/coverage-set-for-nasa-s-spacex-crew-7-events-broadcast-launch" >🔗</a> **[NASA]** Coverage Set for NASA’s SpaceX Crew-7 Events, Broadcast, Launch


  - <a href="https://go4liftoff.com/launch/id/1caacff9-837e-493b-afd4-4da54eeccdf2" >🚀</a> **Falcon 9 Block 5 | Crew-7** from Kennedy Space Center, FL, USA




  - <a href="https://go4liftoff.com/event/id/851" >📆</a> **Crew-7 Arrival at Kennedy**

  - <a href="https://go4liftoff.com/event/id/852" >📆</a> **Crew-7 Flight Readiness Review teleconference**

  - <a href="https://go4liftoff.com/event/id/853" >📆</a> **Crew-7 Postlaunch News Conference**

  - <a href="https://go4liftoff.com/event/id/768" >📆</a> **SpaceX Crew-7 Crew Dragon Docking**


- <a href="https://spacenews.com/true-anomaly-opens-spacecraft-manufacturing-facility-in-colorado/" >🔗</a> **[SpaceNews]** True Anomaly opens spacecraft manufacturing facility in Colorado


- <a href="https://spacenews.com/space-development-agency-to-consider-commercial-leo-options-to-augment-dod-network/" >🔗</a> **[SpaceNews]** Space Development Agency to consider commercial LEO options to augment DoD network


- <a href="https://europeanspaceflight.com/hyimpulse-to-debut-sr75-rocket-no-earlier-than-december-1/" >🔗</a> **[European Spaceflight]** HyImpulse to Debut SR75 Rocket No Earlier than December 1


- <a href="https://www.cnbc.com/2023/08/17/investing-in-space-a-guide-to-satellites.html" >🔗</a> **[CNBC]** Investing in Space: A guide to satellites




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/the-downlink/storms-and-showers" >🔗</a> **[Planetary Society]** Storms and showers


- <a href="https://blog.ulalaunch.com/blog/silentbarker/nrol-107-countdown-rehearsal-tests-atlas-v" >🔗</a> **[United Launch Alliance]** SILENTBARKER/NROL-107: Countdown rehearsal tests Atlas V rocket


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-august-7-13-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: August 7-13, 2023


- <a href="https://www.planetary.org/the-downlink/hasta-la-vista-baby" >🔗</a> **[Planetary Society]** Hasta la vista, baby


- <a href="https://blog.ulalaunch.com/blog/icps-3-upperstage-that-will-propel-artemis-iii-astronauts-to-the-moon-arrives-for-processing" >🔗</a> **[United Launch Alliance]** ICPS-3: Upperstage that will propel Artemis III astronauts to the Moon arrives for processing


- <a href="https://www.planetary.org/articles/exoplanet-terminator-zones-search-for-life" >🔗</a> **[Planetary Society]** Are exoplanet 'terminator zones' a lead in the search for life?


- <a href="https://blog.ulalaunch.com/blog/icps-2-orion-will-observe-upper-stage-after-launch" >🔗</a> **[United Launch Alliance]** ICPS-2: Rendezvous target guides Artemis II Orion demonstrations


  - <a href="https://go4liftoff.com/launch/id/41699701-2ef4-4b0c-ac9d-6757820cde87" >🚀</a> **SLS Block 1 | Artemis II** from Kennedy Space Center, FL, USA



- <a href="https://europeanspaceflight.substack.com/p/to-stream-or-not-to-stream" >🔗</a> **[European Spaceflight]** To stream or not to stream


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-july-24-august-6-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: July 24-August 6, 2023


- <a href="https://www.planetary.org/the-downlink/far-out-man" >🔗</a> **[Planetary Society]** Far out, man!




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230818T181626">2023-08-18 18:16:26 UTC</a>
  <br>
</div>