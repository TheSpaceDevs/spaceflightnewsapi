![Cover](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/snapi_poster.png)

[![Website](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/badge_snapi_website.svg)](https://spaceflightnewsapi.net/)
[![Documentation](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/badge_snapi_doc.svg)](https://api.spaceflightnewsapi.net/v4/docs)
[![Version](https://img.shields.io/github/v/release/TheSpaceDevs/spaceflightnewsapi?style=for-the-badge)](https://github.com/TheSpaceDevs/spaceflightnewsapi/releases/tag/v4.0.3)
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
- <a href="https://europeanspaceflight.com/thermal-data-startup-constellr-extends-seed-round-to-e17m/" >🔗</a> **[European Spaceflight]** Thermal Data Startup Constellr Extends Seed Round to €17M


- <a href="https://spacepolicyonline.com/news/whats-happening-in-space-policy-july-23-29-2023/" >🔗</a> **[SpacePolicyOnline.com]** What’s Happening in Space Policy July 23-29, 2023


- <a href="https://tlpnetwork.com/news/2023/07/gaganyaan_mission_moves_closer_to_spaceflight" >🔗</a> **[The Launch Pad]** ISRO Begins Gaganyaan Crew Capsule Recovery Trials With Indian Navy


  - <a href="https://go4liftoff.com/launch/id/dfac5ab7-7017-454f-b6cf-eeed277a97b5" >🚀</a> **LVM-3 | Gaganyaan-1** from Satish Dhawan Space Centre, India



- <a href="https://spacenews.com/nasa-offers-details-on-commercial-space-capabilities-agreements/" >🔗</a> **[SpaceNews]** NASA offers details on commercial space capabilities agreements


- <a href="https://www.teslarati.com/spacex-launch-22-version-2-mini-starlink-satellites/" >🔗</a> **[Teslarati]** SpaceX to launch 22 Version 2 mini Starlink satellites


  - <a href="https://go4liftoff.com/launch/id/c407b340-49e6-447a-b872-8441618f0ec7" >🚀</a> **Falcon 9 Block 5 | Starlink Group 6-6** from Cape Canaveral, FL, USA



- <a href="https://tlpnetwork.com/news/2023/07/shenzhou-16-completes-first-spacewalk-aboard-tiangong-station" >🔗</a> **[The Launch Pad]** Shenzhou 16 Completes First Spacewalk Aboard Tiangong Station


  - <a href="https://go4liftoff.com/launch/id/2f8aff8b-85da-42bf-84eb-6d3b10184c44" >🚀</a> **Long March 2F/G | Shenzhou 16** from Jiuquan Satellite Launch Center, People's Republic of China



- <a href="https://www.nasaspaceflight.com/2023/07/nssl-phase-three-update/" >🔗</a> **[NASASpaceflight]** Space Force releases NSSL phase three second draft


- <a href="https://tlpnetwork.com/news/2023/07/first-astranis-satellite-suffers-deployment-glitch" >🔗</a> **[The Launch Pad]** First Astranis Satellite Suffers Deployment Glitch


  - <a href="https://go4liftoff.com/launch/id/8b1067dd-81c6-4bc3-b0f1-45f78963716f" >🚀</a> **Falcon Heavy | ViaSat-3 Americas & Others** from Kennedy Space Center, FL, USA



- <a href="https://tlpnetwork.com/news/2023/07/amazon-to-open-new-project-kuiper-processing-facility-at-nasa-kennedy-space-center" >🔗</a> **[The Launch Pad]** Amazon To Open New Project Kuiper Processing Facility at NASA Kennedy Space Center


- <a href="https://www.cnbc.com/2023/07/22/space-force-raises-the-stakes-in-nssl-race-for-military-launches.html" >🔗</a> **[CNBC]** Space Force raises the stakes as rocket companies compete for lucrative military missions




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/the-downlink/thats-a-mare" >🔗</a> **[Planetary Society]** That’s a mare


- <a href="https://www.planetary.org/articles/the-senate-threatens-to-cancel-mars-sample-return" >🔗</a> **[Planetary Society]** The U.S. Senate threatens to cancel Mars Sample Return


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-july-3-16-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: July 3-16, 2023


- <a href="https://europeanspaceflight.substack.com/p/a-little-boost-goes-a-long-way" >🔗</a> **[European Spaceflight]** A little Boost! goes a long way


- <a href="https://www.planetary.org/the-downlink/speedy-spacecraft-and-pretty-pics" >🔗</a> **[Planetary Society]** Speedy spacecraft and pretty pics


- <a href="https://www.planetary.org/space-missions/chandrayaan-3" >🔗</a> **[Planetary Society]** Chandrayaan-3, India's Moon lander and rover


- <a href="https://europeanspaceflight.substack.com/p/what-will-become-of-the-german-north" >🔗</a> **[European Spaceflight]** What will become of the German North Sea floating launch site?


- <a href="https://www.planetary.org/advocacy-action-center" >🔗</a> **[Planetary Society]** Advocacy Action Center


- <a href="https://www.planetary.org/sci-tech/studying-salty-earth-lakes" >🔗</a> **[Planetary Society]** Studying salty Earth lakes to learn about other worlds


- <a href="https://www.planetary.org/sci-tech/growing-veggies-moon-mars" >🔗</a> **[Planetary Society]** Growing veggies for the Moon and Mars




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230724T061910">2023-07-24 06:19:10 UTC</a>
  <br>
</div>