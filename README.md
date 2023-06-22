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
- <a href="https://europeanspaceflight.com/cnes-awards-contract-to-dark-for-space-debris-interceptor-simulation/" >🔗</a> **[European Spaceflight]** CNES Awards Contract to Dark for Space Debris Interceptor Simulation


- <a href="https://tlpnetwork.com/news/2023/06/intelsat-ends-merger-negotiations-with-ses" >🔗</a> **[The Launch Pad]** Intelsat Ends Merger Negotiations with SES


- <a href="https://tlpnetwork.com/news/2023/06/northstar-signs-multi-launch-deal-with-rocketlab-following-virgin-orbit-collapse" >🔗</a> **[The Launch Pad]** NorthStar Signs Multi Launch Deal With RocketLab Following Virgin Orbit Collapse


- <a href="https://spacenews.com/northstar-pivots-to-rocket-lab-following-virgin-orbits-collapse/" >🔗</a> **[SpaceNews]** NorthStar pivots to Rocket Lab following Virgin Orbit’s collapse


- <a href="https://tlpnetwork.com/news/2023/06/spacelogistics-secures-3-orders-for-robotic-maintenance-and-boosting-spacecraft-set-to-launch-2025" >🔗</a> **[The Launch Pad]** SpaceLogistics Secures 3 Orders For New Robotic Maintenance & Boosting Spacecraft Set To Launch 2025


- <a href="https://tlpnetwork.com/news/2023/06/kuva-space-wins-hyperspectral-data-award" >🔗</a> **[The Launch Pad]** Kuva Space Wins Hyperspectral Data Award


- <a href="https://spacepolicyonline.com/news/glaze-spells-out-priorities-if-budget-cuts-materialize/" >🔗</a> **[SpacePolicyOnline.com]** Glaze Spells Out Priorities if Budget Cuts Materialize


- <a href="https://spacenews.com/ecuador-signs-artemis-accords/" >🔗</a> **[SpaceNews]** Ecuador signs Artemis Accords


- <a href="https://www.nasaspaceflight.com/2023/06/ship-25-engine-testing/" >🔗</a> **[NASASpaceflight]** Ship 25 begins engine testing as Starship launch pad work continues


  - <a href="https://go4liftoff.com/launch/id/04b91bb8-38a7-4868-b025-4bbe05d1fbfe" >🚀</a> **Starship | Integrated Flight Test 2** from SpaceX Space Launch Facility, TX, USA



- <a href="https://arstechnica.com/science/2023/06/the-atlantic-tropics-are-on-fire-it-already-looks-a-like-august-out-there/" >🔗</a> **[Arstechnica]** The Atlantic tropics are on fire—it already looks like August out there




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/articles/citizen-astronomer-asteroid-defender-tips" >🔗</a> **[Planetary Society]** Want to be a citizen astronomer and defend Earth from asteroids? Here are some tips.


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-june-12-19-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: June 12-19, 2023


- <a href="https://europeanspaceflight.substack.com/p/reusability-efforts-of-european-launch" >🔗</a> **[European Spaceflight]** Reusability efforts of European launch startups


- <a href="https://www.planetary.org/the-downlink/day-and-night-its-all-about-starlight" >🔗</a> **[Planetary Society]** Day and night, it’s all about starlight


- <a href="https://blog.ulalaunch.com/blog/rocketstars-leading-the-engineering-team-for-delta-iv-heavy" >🔗</a> **[United Launch Alliance]** RocketStars: Leading the engineering team for Delta IV Heavy


- <a href="https://www.planetary.org/articles/vladimir-benishek-asteroid-research" >🔗</a> **[Planetary Society]** Vladimir Benishek and the mystique of asteroid research


- <a href="https://blog.ulalaunch.com/blog/nrol-68-delta-iv-heavy-readied-for-national-security-launch" >🔗</a> **[United Launch Alliance]** NROL-68: Delta IV Heavy readied for national security launch


- <a href="https://blog.ulalaunch.com/blog/how-to-fix-the-pollution-of-orbital-debris" >🔗</a> **[United Launch Alliance]** How to Fix the Pollution of Orbital Debris


- <a href="https://www.planetary.org/advocacy/day-of-action-2023-participant-information" >🔗</a> **[Planetary Society]** Day of Action 2023 - Participant Information


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-june-5-11-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: June 5-11, 2023




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230622T071648">2023-06-22 07:16:48 UTC</a>
  <br>
</div>