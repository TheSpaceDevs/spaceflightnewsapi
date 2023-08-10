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
- <a href="https://spacenews.com/space-force-tries-to-hedge-risk-with-new-launch-strategy/" >🔗</a> **[SpaceNews]** Space Force tries to hedge risk with new launch strategy


- <a href="https://spacenews.com/scout-space-stanford-university-win-space-force-contract-extension/" >🔗</a> **[SpaceNews]** Scout Space, Stanford University win Space Force contract extension


- <a href="https://spacenews.com/chinese-startup-launches-7th-ceres-1-rocket-preps-for-first-sea-launch/" >🔗</a> **[SpaceNews]** Chinese startup launches 7th Ceres-1 rocket, preps for first sea launch


  - <a href="https://go4liftoff.com/launch/id/d7131f47-a962-4832-ae68-52a57bb0b684" >🚀</a> **Ceres-1 | 7 satellites** from Jiuquan Satellite Launch Center, People's Republic of China



- <a href="https://arstechnica.com/space/2023/08/its-finally-time-virgin-galactic-is-flying-private-astronauts-into-space/" >🔗</a> **[Arstechnica]** It’s finally time—Virgin Galactic is flying private astronauts into space


  - <a href="https://go4liftoff.com/launch/id/6229654f-e7ea-4d97-80f7-0195161e8645" >🚀</a> **SpaceShipTwo | Galactic 02** from Air launch to Suborbital flight



- <a href="https://spacenews.com/viasat-not-ready-to-declare-viasat-3-americas-a-total-loss/" >🔗</a> **[SpaceNews]** Viasat not ready to declare Viasat-3 Americas a total loss


  - <a href="https://go4liftoff.com/launch/id/8b1067dd-81c6-4bc3-b0f1-45f78963716f" >🚀</a> **Falcon Heavy | ViaSat-3 Americas & Others** from Kennedy Space Center, FL, USA



- <a href="https://spacenews.com/japans-interstellar-aims-for-orbital-launch-in-2025/" >🔗</a> **[SpaceNews]** Japan’s Interstellar aims for orbital launch in 2025


- <a href="https://spacenews.com/u-s-intelligence-agencies-take-steps-to-protect-commercial-satellite-operators/" >🔗</a> **[SpaceNews]** U.S. intelligence agencies take steps to protect commercial satellites


- <a href="https://www.cnbc.com/2023/08/09/viasat-vsat-q1-earnings-report.html" >🔗</a> **[CNBC]** Viasat revenue grows as investigation continues into malfunctioning $750 million satellite


  - <a href="https://go4liftoff.com/launch/id/8b1067dd-81c6-4bc3-b0f1-45f78963716f" >🚀</a> **Falcon Heavy | ViaSat-3 Americas & Others** from Kennedy Space Center, FL, USA



- <a href="https://spacenews.com/lynk-global-starts-initial-direct-to-device-services-in-the-cook-islands/" >🔗</a> **[SpaceNews]** Lynk Global starts initial direct-to-device services in the Cook Islands


- <a href="https://spacenews.com/esa-confirms-ariane-6-debut-to-slip-to-2024/" >🔗</a> **[SpaceNews]** ESA confirms Ariane 6 debut to slip to 2024


  - <a href="https://go4liftoff.com/launch/id/3e461ec0-8b64-4804-b9aa-e1e1f066065a" >🚀</a> **Ariane 62 | Maiden Flight** from Kourou, French Guiana





## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/articles/exoplanet-terminator-zones-search-for-life" >🔗</a> **[Planetary Society]** Are exoplanet 'terminator zones' a lead in the search for life?


- <a href="https://blog.ulalaunch.com/blog/icps-2-orion-will-observe-upper-stage-after-launch" >🔗</a> **[United Launch Alliance]** ICPS-2: Rendezvous target guides Artemis II Orion demonstrations


- <a href="https://europeanspaceflight.substack.com/p/to-stream-or-not-to-stream" >🔗</a> **[European Spaceflight]** To stream or not to stream


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-july-24-august-6-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: July 24-August 6, 2023


- <a href="https://www.planetary.org/the-downlink/far-out-man" >🔗</a> **[Planetary Society]** Far out, man!


- <a href="https://blog.ulalaunch.com/blog/silentbarker-atlas-v-stacked-for-national-security-launch" >🔗</a> **[United Launch Alliance]** SILENTBARKER/NROL-107: Atlas V stacked for national security launch


- <a href="https://europeanspaceflight.substack.com/p/will-esa-finally-land-on-mars" >🔗</a> **[European Spaceflight]** Will ESA finally land on Mars?


- <a href="https://www.planetary.org/mission-control" >🔗</a> **[Planetary Society]** LightSail 2 Mission Control


- <a href="https://www.planetary.org/the-downlink/aquatic-equivalencies" >🔗</a> **[Planetary Society]** Aquatic equivalencies


- <a href="https://www.planetary.org/articles/life-on-venus-your-questions-answered" >🔗</a> **[Planetary Society]** Life on Venus: Your Questions Answered




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230810T141334">2023-08-10 14:13:34 UTC</a>
  <br>
</div>