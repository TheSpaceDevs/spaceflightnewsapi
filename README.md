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
- <a href="https://spacenews.com/space-leasing-international-sets-sights-on-ground-stations-satellites-an-launch-infrastructure/" >🔗</a> **[SpaceNews]** Space Leasing International sets sights on ground stations, satellites an launch infrastructure


- <a href="https://www.teslarati.com/spacex-falcon-9-launches-56-starlink-satellites/" >🔗</a> **[Teslarati]** SpaceX Falcon 9 launches 56 Starlink satellites


- <a href="https://arstechnica.com/space/2023/06/the-mars-sample-return-mission-is-starting-to-give-nasa-sticker-shock/" >🔗</a> **[Arstechnica]** NASA’s Mars Sample Return has a new price tag—and it’s colossal


- <a href="https://tlpnetwork.com/news/2023/06/arianespace-back-on-track-for-final-ariane-5-launch" >🔗</a> **[The Launch Pad]** Arianespace Back On Track For Final Ariane 5 Launch


  - <a href="https://go4liftoff.com/launch/id/e3f8e755-0867-413a-a05a-15ca06ce7fa3" >🚀</a> **Ariane 5 ECA+ | Syracuse 4B & Heinrich Hertz (H2Sat)** from Kourou, French Guiana



- <a href="http://www.nasa.gov/press-release/nasa-invites-media-to-cover-asteroid-sample-return-logistics-call" >🔗</a> **[NASA]** NASA Invites Media to Cover Asteroid Sample Return, Logistics Call


  - <a href="https://go4liftoff.com/launch/id/0bcc6850-4c51-4b08-aa19-0b3753351b9b" >🚀</a> **Atlas V 411 | OSIRIS-REx** from Cape Canaveral, FL, USA




  - <a href="https://go4liftoff.com/event/id/36" >📆</a> **OSIRIS-Rex Sample Return**


- <a href="https://spacenews.com/ovzon-3-on-course-to-miss-regulatory-deadline-after-latest-delay/" >🔗</a> **[SpaceNews]** Ovzon 3 on course to miss regulatory deadline after latest delay


  - <a href="https://go4liftoff.com/launch/id/1d374bef-0e4e-4b3f-b45b-25c14aaa2b0e" >🚀</a> **Falcon 9 Block 5 | Ovzon-3** from Cape Canaveral, FL, USA



- <a href="https://spacenews.com/apex-raises-16-million-for-spacecraft-factory/" >🔗</a> **[SpaceNews]** Apex raises $16 million for spacecraft factory


- <a href="https://arstechnica.com/space/2023/06/rocket-report-electron-scoops-up-virgin-launch-ula-flies-first-2023-mission/" >🔗</a> **[Arstechnica]** Rocket Report: Electron scoops up Virgin launch, ULA flies first 2023 mission


  - <a href="https://go4liftoff.com/launch/id/8cfa00a5-a72e-48b7-80bd-944664688f59" >🚀</a> **Delta IV Heavy | NROL-68** from Cape Canaveral, FL, USA

  - <a href="https://go4liftoff.com/launch/id/89f9600b-b250-4b0f-a713-99b123bb58d8" >🚀</a> **Electron | NorthStar 1** from Onenui Station, Mahia Peninsula, New Zealand

  - <a href="https://go4liftoff.com/launch/id/bc939d6c-4f57-44d8-8caf-dd81c0872a9e" >🚀</a> **Electron | NorthStar 2** from Onenui Station, Mahia Peninsula, New Zealand

  - <a href="https://go4liftoff.com/launch/id/cd10c1a7-886f-427d-a653-106001da54d6" >🚀</a> **Electron | NorthStar 3** from Onenui Station, Mahia Peninsula, New Zealand



- <a href="https://spacenews.com/safran-and-terran-orbital-to-explore-joint-production-of-satellite-propulsion-systems-in-the-u-s/" >🔗</a> **[SpaceNews]** Safran, Terran Orbital to explore joint production of satellite propulsion systems


- <a href="https://spacenews.com/u-s-and-india-to-expand-spaceflight-cooperation/" >🔗</a> **[SpaceNews]** U.S. and India to expand spaceflight cooperation




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/the-downlink/rings-and-dings" >🔗</a> **[Planetary Society]** Rings and dings


- <a href="https://blog.ulalaunch.com/blog/united-launch-alliance-successfully-launches-the-penultimate-delta-iv-heavy-rocket" >🔗</a> **[United Launch Alliance]** NROL-68: United Launch Alliance Successfully Launches the Penultimate Delta IV Heavy Rocket


- <a href="https://www.planetary.org/articles/ariel-barreiro-interview" >🔗</a> **[Planetary Society]** Marrying the arts and science in space


- <a href="https://www.planetary.org/articles/citizen-astronomer-asteroid-defender-tips" >🔗</a> **[Planetary Society]** Want to be a citizen astronomer and defend Earth from asteroids? Here are some tips.


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-june-12-19-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: June 12-19, 2023


- <a href="https://europeanspaceflight.substack.com/p/reusability-efforts-of-european-launch" >🔗</a> **[European Spaceflight]** Reusability efforts of European launch startups


- <a href="https://www.planetary.org/the-downlink/day-and-night-its-all-about-starlight" >🔗</a> **[Planetary Society]** Day and night, it’s all about starlight


- <a href="https://blog.ulalaunch.com/blog/rocketstars-leading-the-engineering-team-for-delta-iv-heavy" >🔗</a> **[United Launch Alliance]** RocketStars: Leading the engineering team for Delta IV Heavy


- <a href="https://www.planetary.org/articles/vladimir-benishek-asteroid-research" >🔗</a> **[Planetary Society]** Vladimir Benishek and the mystique of asteroid research


- <a href="https://blog.ulalaunch.com/blog/nrol-68-delta-iv-heavy-readied-for-national-security-launch" >🔗</a> **[United Launch Alliance]** NROL-68: Delta IV Heavy readied for national security launch




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230623T201651">2023-06-23 20:16:51 UTC</a>
  <br>
</div>