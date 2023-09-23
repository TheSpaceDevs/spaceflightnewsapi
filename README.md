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
- <a href="https://spacenews.com/office-of-space-commerce-touts-progress-on-civil-space-traffic-coordination-system/" >🔗</a> **[SpaceNews]** Office of Space Commerce touts progress on civil space traffic coordination system


- <a href="https://spacenews.com/air-force-validates-boeings-new-wgs-satellite/" >🔗</a> **[SpaceNews]** Air Force validates Boeing’s new WGS satellite


- <a href="https://spacenews.com/nasa-ready-for-osiris-rex-sample-return/" >🔗</a> **[SpaceNews]** NASA ready for OSIRIS-REx sample return


  - <a href="https://go4liftoff.com/launch/id/0bcc6850-4c51-4b08-aa19-0b3753351b9b" >🚀</a> **Atlas V 411 | OSIRIS-REx** from Cape Canaveral, FL, USA




  - <a href="https://go4liftoff.com/event/id/36" >📆</a> **OSIRIS-Rex Sample Return**


- <a href="https://tlpnetwork.com/news/2023/09/sierra-space-conducts-5th-life-module-burst-test" >🔗</a> **[The Launch Pad]** Sierra Space Conducts 5th LIFE Module Burst Test


- <a href="https://tlpnetwork.com/news/2023/09/chinas-galactic-energy-experiences-first-launch-failure" >🔗</a> **[The Launch Pad]** China's Galactic Energy Experiences First Launch Failure


  - <a href="https://go4liftoff.com/launch/id/6eef3c8d-90a9-499c-96cd-e42326722d12" >🚀</a> **Ceres-1 | Jilin-1 High Resolution 04B** from Jiuquan Satellite Launch Center, People's Republic of China



- <a href="http://www.nasa.gov/press-release/nasa-scientists-to-discuss-oct-14-ring-of-fire-solar-eclipse" >🔗</a> **[NASA]** NASA Scientists to Discuss Oct. 14 'Ring of Fire' Solar Eclipse



  - <a href="https://go4liftoff.com/event/id/857" >📆</a> **2023 Annular Solar Eclipse**


- <a href="https://spacenews.com/satellogic-relocating-to-the-united-states-in-search-of-government-growth/" >🔗</a> **[SpaceNews]** Satellogic relocating to the United States in search of government growth


- <a href="https://www.nasaspaceflight.com/2023/09/starship-upgrades-upcoming-test-flight/" >🔗</a> **[NASASpaceflight]** Pending FAA approval, Starship ready to sport upgrades for upcoming test flight


  - <a href="https://go4liftoff.com/launch/id/04b91bb8-38a7-4868-b025-4bbe05d1fbfe" >🚀</a> **Starship | Integrated Flight Test 2** from SpaceX Space Launch Facility, TX, USA



- <a href="http://www.nasa.gov/press-release/record-setting-nasa-astronaut-soon-returns-to-earth-watch-live" >🔗</a> **[NASA]** Record-Setting NASA Astronaut Soon Returns to Earth; Watch Live


  - <a href="https://go4liftoff.com/launch/id/bc73ec4f-633e-4eb5-8b8e-5c996ea1733f" >🚀</a> **Soyuz 2.1a | Soyuz MS-22** from Baikonur Cosmodrome, Republic of Kazakhstan

  - <a href="https://go4liftoff.com/launch/id/e3290e0e-d967-4a5d-95eb-f8fae06a9034" >🚀</a> **Soyuz 2.1a | Soyuz MS-23** from Baikonur Cosmodrome, Republic of Kazakhstan



- <a href="https://europeanspaceflight.com/spain-partner-with-esa-to-build-80m-euro-atlantic-constellation/" >🔗</a> **[European Spaceflight]** Spain Partner with ESA to Build €80M Atlantic Constellation




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/the-downlink/equinox-and-equilux" >🔗</a> **[Planetary Society]** Equinox and equilux


- <a href="https://www.planetary.org/articles/what-is-an-annular-solar-eclipse" >🔗</a> **[Planetary Society]** What is an annular solar eclipse?


- <a href="https://www.planetary.org/articles/the-day-of-action-returns-to-capitol-hill" >🔗</a> **[Planetary Society]** The Day of Action returns to Capitol Hill


- <a href="https://www.planetary.org/articles/tips-for-2024-total-solar-eclipse" >🔗</a> **[Planetary Society]** Want to experience the 2024 total solar eclipse? Here are some tips.


- <a href="https://blog.ulalaunch.com/blog/protoflight-atlas-v-stacked-ahead-of-first-kuiper-launch" >🔗</a> **[United Launch Alliance]** Protoflight: Atlas V stacked ahead of first Kuiper launch


- <a href="https://europeanspaceflight.substack.com/p/is-there-a-future-for-the-european" >🔗</a> **[European Spaceflight]** Is there a future for the European Astronaut Corps?


- <a href="https://www.planetary.org/the-downlink/lost-and-found" >🔗</a> **[Planetary Society]** Lost and found


- <a href="https://www.planetary.org/articles/guide-to-eclipse-vocabulary" >🔗</a> **[Planetary Society]** A guide to eclipse vocabulary


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-september-4-10-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: September 4-10, 2023


- <a href="https://www.planetary.org/the-downlink/cometary-sights-and-sounds" >🔗</a> **[Planetary Society]** Cometary sights and sounds




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230923T122419">2023-09-23 12:24:19 UTC</a>
  <br>
</div>