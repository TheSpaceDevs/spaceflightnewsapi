![Cover](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/snapi_poster.png)

[![Website](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/badge_snapi_website.svg)](https://spaceflightnewsapi.net/)
[![Documentation](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/badge_snapi_doc.svg)](https://api.spaceflightnewsapi.net/v4/docs)
[![Version](https://img.shields.io/github/v/release/TheSpaceDevs/spaceflightnewsapi?style=for-the-badge)](https://github.com/TheSpaceDevs/spaceflightnewsapi/releases/tag/v4.0.2)
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
- <a href="https://spacenews.com/firefly-to-buy-remaining-virgin-orbit-assets/" >🔗</a> **[SpaceNews]** Firefly to buy remaining Virgin Orbit assets


- <a href="https://www.nasaspaceflight.com/2023/06/nasa-low-earth-orbit-partnerships/" >🔗</a> **[NASASpaceflight]** SpaceX, Blue Origin, others highlighted in new NASA low-Earth orbit partnerships


- <a href="http://www.nasa.gov/press-release/nasa-invites-media-to-view-orion-spacecraft-for-next-artemis-missions" >🔗</a> **[NASA]** NASA Invites Media to View Orion Spacecraft for Next Artemis Missions


  - <a href="https://go4liftoff.com/launch/id/41699701-2ef4-4b0c-ac9d-6757820cde87" >🚀</a> **SLS Block 1 | Artemis II** from Kennedy Space Center, FL, USA



- <a href="https://spacenews.com/intelligence-analysts-confront-the-reality-of-deepfakes/" >🔗</a> **[SpaceNews]** Intelligence analysts confront the reality of deepfakes


- <a href="https://spacenews.com/nasa-agreements-to-support-work-on-commercial-spacecraft-and-space-stations/" >🔗</a> **[SpaceNews]** NASA agreements to support work on commercial spacecraft and space stations


- <a href="https://spacenews.com/cesiumastro-to-develop-satcom-terminal-for-u-s-air-force-reaper-drone/" >🔗</a> **[SpaceNews]** CesiumAstro to develop satcom terminal for U.S. Air Force drone


- <a href="https://arstechnica.com/space/2023/06/rocket-report-final-ariane-5-launch-delayed-virgin-galactic-set-to-fly-again/" >🔗</a> **[Arstechnica]** Rocket Report: China addresses falling rocket debris, Vulcan launch slipping


- <a href="https://spacenews.com/technical-problem-postpones-final-ariane-5-launch/" >🔗</a> **[SpaceNews]** Technical problem postpones final Ariane 5 launch


  - <a href="https://go4liftoff.com/launch/id/e3f8e755-0867-413a-a05a-15ca06ce7fa3" >🚀</a> **Ariane 5 ECA+ | Syracuse 4B & Heinrich Hertz (H2Sat)** from Kourou, French Guiana



- <a href="https://spacenews.com/eutelsat-reversing-course-with-european-retail-business-sale/" >🔗</a> **[SpaceNews]** Eutelsat reversing course with European retail broadband business sale


- <a href="https://tlpnetwork.com/news/2023/06/nasa-partners-with-7-companies-for-future-commercial-space-capabilities" >🔗</a> **[The Launch Pad]** BREAKING! NASA Partners With SpaceX, Blue Origin, Sierra Space + 4 Others For Future Commercial Space Capabilities




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/the-downlink/day-and-night-its-all-about-starlight" >🔗</a> **[Planetary Society]** Day and night, it’s all about starlight


- <a href="https://blog.ulalaunch.com/blog/rocketstars-leading-the-engineering-team-for-delta-iv-heavy" >🔗</a> **[United Launch Alliance]** RocketStars: Leading the engineering team for Delta IV Heavy


- <a href="https://www.planetary.org/articles/vladimir-benishek-asteroid-research" >🔗</a> **[Planetary Society]** Vladimir Benishek and the mystique of asteroid research


- <a href="https://blog.ulalaunch.com/blog/nrol-68-delta-iv-heavy-readied-for-national-security-launch" >🔗</a> **[United Launch Alliance]** NROL-68: Delta IV Heavy readied for national security launch


- <a href="https://blog.ulalaunch.com/blog/how-to-fix-the-pollution-of-orbital-debris" >🔗</a> **[United Launch Alliance]** How to Fix the Pollution of Orbital Debris


- <a href="https://www.planetary.org/advocacy/day-of-action-2023-participant-information" >🔗</a> **[Planetary Society]** Day of Action 2023 - Participant Information


- <a href="https://www.planetary.org/articles/why-did-we-need-osiris-rex" >🔗</a> **[Planetary Society]** Why did we need OSIRIS-REx?


- <a href="https://www.planetary.org/articles/your-impact-june-solstice-2023" >🔗</a> **[Planetary Society]** Your impact: June solstice 2023


- <a href="https://www.planetary.org/articles/asteroid-samples-from-another-world" >🔗</a> **[Planetary Society]** Asteroid samples from another world


- <a href="https://www.planetary.org/the-downlink/the-scientific-truth-is-out-there" >🔗</a> **[Planetary Society]** The scientific truth is out there




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230616T181713">2023-06-16 18:17:13 UTC</a>
  <br>
</div>