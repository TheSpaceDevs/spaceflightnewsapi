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
- <a href="https://tlpnetwork.com/news/2023/07/eso-elt-50-percent-complete" >🔗</a> **[The Launch Pad]** ESO's Extremely Large Telescope Reaches 50% Complete Milestone


- <a href="https://tlpnetwork.com/news/2023/07/landspace-zhuque-2-reaches-orbit-wins-methalox-space-race" >🔗</a> **[The Launch Pad]** BREAKING! Landspace Zhuque-2 Reaches Orbit, China Wins Methalox Space Race


- <a href="https://tlpnetwork.com/news/2023/07/nasa-artemis-crew-transport-vehicles-arrive-at-kennedy-space-center" >🔗</a> **[The Launch Pad]** NASA's Artemis Crew Transport Vehicles Arrive At Kennedy Space Center


- <a href="https://spacenews.com/u-s-sharpens-plan-for-military-space-race/" >🔗</a> **[SpaceNews]** U.S. sharpens plan for military space race


- <a href="https://tlpnetwork.com/news/2023/07/astranis-announces-contract-to-bring-internet-to-2-million-people-in-philippines-next-year" >🔗</a> **[The Launch Pad]** Astranis Announces Contract To Bring Internet To 2 Million People In Philippines Next Year


- <a href="https://tlpnetwork.com/news/2023/07/nasa-astronaut-garrett-reisman-joins-vast-as-human-spaceflight-advisor" >🔗</a> **[The Launch Pad]** NASA Astronaut Garrett Reisman Joins VAST as Human Spaceflight Advisor


- <a href="https://tlpnetwork.com/news/2023/07/voyager-space-announces-mou-with-india-to-explore-gaganyaan-missions-to-starlab" >🔗</a> **[The Launch Pad]** Voyager Space Announces MoU With India To Explore Gaganyaan Missions To StarLab


- <a href="https://tlpnetwork.com/news/2023/07/nasa-cancels-janus-mission-after-launch-postponement" >🔗</a> **[The Launch Pad]** NASA Cancels Janus Mission After Launch Postponement


  - <a href="https://go4liftoff.com/launch/id/66133437-db31-4098-8e3e-cf34c8125f9b" >🚀</a> **Falcon Heavy | Psyche** from Kennedy Space Center, FL, USA



- <a href="https://www.nasaspaceflight.com/2023/07/zhuque-2-launch2/" >🔗</a> **[NASASpaceflight]** LandSpace claims win in the methane race to orbit via second ZhuQue-2 launch


- <a href="https://www.cnbc.com/2023/07/11/jeff-bezos-blue-origin-be-4-rocket-engine-explodes-during-testing.html" >🔗</a> **[CNBC]** Jeff Bezos’ Blue Origin rocket engine explodes during testing


  - <a href="https://go4liftoff.com/launch/id/a67b40f9-cfcc-4614-a355-a156280b4bb3" >🚀</a> **Vulcan VC4L | Dream Chaser CRS 2 Flight 1** from Cape Canaveral, FL, USA





## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/space-missions/chandrayaan-3" >🔗</a> **[Planetary Society]** Chandrayaan-3, India's Moon lander and rover


- <a href="https://europeanspaceflight.substack.com/p/what-will-become-of-the-german-north" >🔗</a> **[European Spaceflight]** What will become of the German North Sea floating launch site?


- <a href="https://www.planetary.org/sci-tech/studying-salty-earth-lakes" >🔗</a> **[Planetary Society]** Studying salty Earth lakes to learn about other worlds


- <a href="https://www.planetary.org/sci-tech/growing-veggies-moon-mars" >🔗</a> **[Planetary Society]** Growing veggies for the Moon and Mars


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-june-26-july-2-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: June 26-July 2, 2023


- <a href="https://europeanspaceflight.substack.com/p/what-does-the-future-hold-for-the" >🔗</a> **[European Spaceflight]** What does the future hold for the Guiana Space Center?


- <a href="https://www.planetary.org/the-downlink/searching-the-skies-to-keep-us-all-alive" >🔗</a> **[Planetary Society]** Searching the skies to keep us all alive


- <a href="https://www.planetary.org/articles/whats-going-on-with-mars-sample-return" >🔗</a> **[Planetary Society]** What’s going on with Mars Sample Return?


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-june-19-25-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: June 19-25, 2023


- <a href="https://www.planetary.org/articles/announcing-the-2023-shoemaker-neo-grant-winners" >🔗</a> **[Planetary Society]** Announcing the 2023 Shoemaker NEO grant winners




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230712T041900">2023-07-12 04:19:00 UTC</a>
  <br>
</div>