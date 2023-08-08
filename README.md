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
- <a href="https://spacenews.com/solestial-to-supply-solar-arrays-for-atomos-space-tugs/" >🔗</a> **[SpaceNews]** Solestial to supply solar arrays for Atomos space tugs


- <a href="https://tlpnetwork.com/news/2023/08/starliner-cft-delayed-to-2024" >🔗</a> **[The Launch Pad]** Boeing Starliner Crewed Flight Test Delayed To 2024


  - <a href="https://go4liftoff.com/launch/id/968067d1-8c12-4018-9854-b7b7d4bddc6b" >🚀</a> **Atlas V N22 | CST-100 Starliner Crewed Flight Test** from Cape Canaveral, FL, USA



- <a href="https://tlpnetwork.com/news/2023/08/nanoavionics-prepares-leo-black-hole-research-satellite-for-launch" >🔗</a> **[The Launch Pad]** NanoAvionics Prepares LEO Black Hole Research Satellite For Launch


- <a href="https://spacenews.com/pale-blue-to-supply-thrusters-for-yonsei-university-cubesats/" >🔗</a> **[SpaceNews]** Pale Blue to supply thrusters for Yonsei University cubesats


- <a href="https://spacenews.com/first-starliner-crewed-flight-delayed-to-2024/" >🔗</a> **[SpaceNews]** First Starliner crewed flight delayed to 2024


  - <a href="https://go4liftoff.com/launch/id/968067d1-8c12-4018-9854-b7b7d4bddc6b" >🚀</a> **Atlas V N22 | CST-100 Starliner Crewed Flight Test** from Cape Canaveral, FL, USA



- <a href="https://spacenews.com/eutelsat-and-thaicom-go-halves-on-asia-focused-telecoms-satellite/" >🔗</a> **[SpaceNews]** Eutelsat and Thaicom go halves on Asia-focused telecoms satellite


- <a href="https://tlpnetwork.com/news/2023/08/nasa-tropics-constellation-fully-operational-and-ready-for-hurricane-season" >🔗</a> **[The Launch Pad]** NASA TROPICS Constellation Fully Operational & Ready For Hurricane Season


  - <a href="https://go4liftoff.com/launch/id/e870fe28-c5d5-4c3d-be4f-aaddd061ea18" >🚀</a> **Electron | Rocket Like A Hurricane (TROPICS-2)** from Onenui Station, Mahia Peninsula, New Zealand



- <a href="https://tlpnetwork.com/news/2023/08/hyimpulse-issued-first-lran-from-caa" >🔗</a> **[The Launch Pad]** HyImpulse Issued First Large Rocket Air Navigation Order from CAA


- <a href="https://mars.nasa.gov/news/9457/" >🔗</a> **[NASA]** NASA's Ingenuity Mars Helicopter Flies Again After Unscheduled Landing


  - <a href="https://go4liftoff.com/launch/id/c4db6995-f25f-4608-8eb9-ce95d5226af2" >🚀</a> **Atlas V 541 | Mars 2020 (Perseverance rover & Ingenuity helicopter)** from Cape Canaveral, FL, USA



- <a href="https://tlpnetwork.com/news/2023/08/amazon-moves-project-kuiper-demo-to-atlas-5" >🔗</a> **[The Launch Pad]** Amazon Moves Project Kuiper Demo From Vulcan To Atlas 5


  - <a href="https://go4liftoff.com/launch/id/9086bd21-5422-41b9-a492-963aababd8fd" >🚀</a> **Atlas V 501 | Project Kuiper (Atlas V #1/Demo Mission)** from Cape Canaveral, FL, USA





## Latest Blog Posts 🪧

- <a href="https://europeanspaceflight.substack.com/p/to-stream-or-not-to-stream" >🔗</a> **[European Spaceflight]** To stream or not to stream


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-july-24-august-6-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: July 24-August 6, 2023


- <a href="https://www.planetary.org/the-downlink/far-out-man" >🔗</a> **[Planetary Society]** Far out, man!


- <a href="https://blog.ulalaunch.com/blog/silentbarker-atlas-v-stacked-for-national-security-launch" >🔗</a> **[United Launch Alliance]** SILENTBARKER/NROL-107: Atlas V stacked for national security launch


- <a href="https://europeanspaceflight.substack.com/p/will-esa-finally-land-on-mars" >🔗</a> **[European Spaceflight]** Will ESA finally land on Mars?


- <a href="https://www.planetary.org/mission-control" >🔗</a> **[Planetary Society]** LightSail 2 Mission Control


- <a href="https://www.planetary.org/the-downlink/aquatic-equivalencies" >🔗</a> **[Planetary Society]** Aquatic equivalencies


- <a href="https://www.planetary.org/articles/life-on-venus-your-questions-answered" >🔗</a> **[Planetary Society]** Life on Venus: Your Questions Answered


- <a href="https://europeanspaceflight.substack.com/p/the-time-europe-tried-to-copy-energia" >🔗</a> **[European Spaceflight]** The time Europe tried to copy Energia


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-july-17-23-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: July 17-23, 2023




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230808T091257">2023-08-08 09:12:57 UTC</a>
  <br>
</div>