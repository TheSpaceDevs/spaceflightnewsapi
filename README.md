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
- <a href="https://spacenews.com/nasa-clears-crew-7-mission-for-launch-to-the-space-station/" >🔗</a> **[SpaceNews]** NASA clears Crew-7 mission for launch to the space station


  - <a href="https://go4liftoff.com/launch/id/1caacff9-837e-493b-afd4-4da54eeccdf2" >🚀</a> **Falcon 9 Block 5 | Crew-7** from Kennedy Space Center, FL, USA



- <a href="https://spacepolicyonline.com/news/luna-25s-engines-fired-longer-than-planned/" >🔗</a> **[SpacePolicyOnline.com]** Luna-25’s Engines Fired Longer Than Planned


  - <a href="https://go4liftoff.com/launch/id/2277b184-5a07-4a71-90ce-367f41420eaa" >🚀</a> **Soyuz 2.1b/Fregat-M | Luna 25** from Vostochny Cosmodrome, Siberia, Russian Federation



- <a href="https://www.teslarati.com/weekly-space-recap-august-14-august-20/" >🔗</a> **[Teslarati]** Weekly Space Recap: August 14 – August 20


- <a href="https://spacenews.com/eutelsats-oneweb-merger-now-just-pending-shareholder-vote/" >🔗</a> **[SpaceNews]** Eutelsat’s OneWeb merger now just pending shareholder vote


- <a href="https://www.nasaspaceflight.com/2023/08/launch-roundup-082123/" >🔗</a> **[NASASpaceflight]** Launch Roundup: SpaceX to launch four missions, Progress MS-24 to resupply ISS


  - <a href="https://go4liftoff.com/launch/id/15699687-3fb1-4749-9680-fc858e5e7081" >🚀</a> **Falcon 9 Block 5 | Starlink Group 7-1** from Vandenberg SFB, CA, USA

  - <a href="https://go4liftoff.com/launch/id/87fba73c-f085-4abf-830d-fae92c599977" >🚀</a> **Falcon 9 Block 5 | Starlink Group 6-11** from Cape Canaveral, FL, USA

  - <a href="https://go4liftoff.com/launch/id/92bf99cd-2469-4500-864a-40a9dfc65332" >🚀</a> **Soyuz 2.1a | Progress MS-24 (85P)** from Baikonur Cosmodrome, Republic of Kazakhstan

  - <a href="https://go4liftoff.com/launch/id/1caacff9-837e-493b-afd4-4da54eeccdf2" >🚀</a> **Falcon 9 Block 5 | Crew-7** from Kennedy Space Center, FL, USA

  - <a href="https://go4liftoff.com/launch/id/0be2e9d6-50d5-49dc-b56c-a919b7e0dfd8" >🚀</a> **Falcon 9 Block 5 | O3b mPower 5 & 6** from Cape Canaveral, FL, USA



- <a href="https://arstechnica.com/space/2023/08/putin-wanted-to-make-russia-great-again-in-space-heres-why-he-failed/" >🔗</a> **[Arstechnica]** The failure of Luna 25 cements Putin’s role as a disastrous space leader


  - <a href="https://go4liftoff.com/launch/id/2277b184-5a07-4a71-90ce-367f41420eaa" >🚀</a> **Soyuz 2.1b/Fregat-M | Luna 25** from Vostochny Cosmodrome, Siberia, Russian Federation



- <a href="https://www.cnbc.com/2023/08/21/pentagon-awards-1point5-billion-to-lockheed-martin-northrop-grumman.html" >🔗</a> **[CNBC]** Pentagon space arm awards $1.5 billion contract to Lockheed, Northrop for communications satellites


- <a href="https://spacenews.com/space-development-agency-awards-1-5-billion-to-lockheed-martin-and-northrop-grumman-for-72-satellites/" >🔗</a> **[SpaceNews]** Space Development Agency awards contracts to Lockheed Martin, Northrop Grumman for 72 satellites


- <a href="https://www.cnbc.com/2023/08/21/redwire-sierra-partner-to-make-drugs-on-inflatable-space-habitat.html" >🔗</a> **[CNBC]** Redwire and Sierra team up to make drugs in space on inflatable habitat’s first mission


- <a href="https://www.cnbc.com/2023/08/21/axiom-space-raises-350-million-from-saudi-and-korean-investors.html" >🔗</a> **[CNBC]** Axiom Space raises $350 million from Saudi and Korean investors




## Latest Blog Posts 🪧

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



- <a href="https://europeanspaceflight.substack.com/p/to-stream-or-not-to-stream" >🔗</a> **[European Spaceflight]** To stream or not to stream




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230822T131630">2023-08-22 13:16:30 UTC</a>
  <br>
</div>