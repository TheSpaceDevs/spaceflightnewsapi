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
- <a href="https://spacenews.com/faa-closes-new-shepard-mishap-investigation/" >🔗</a> **[SpaceNews]** FAA closes New Shepard mishap investigation


- <a href="https://spacenews.com/x-bow-to-demonstrate-additive-manufacturing-of-solid-rocket-motors-for-u-s-air-force/" >🔗</a> **[SpaceNews]** X-Bow to demonstrate additive manufacturing of solid rocket motors for U.S. Air Force


- <a href="https://www.cnbc.com/2023/09/27/spacex-wins-first-pentagon-contract-for-starshield.html" >🔗</a> **[CNBC]** SpaceX wins first Pentagon contract for Starshield, its satellite network for military use


- <a href="https://spacenews.com/rogue-space-systems-gets-us-air-force-funds-to-advance-in-orbit-servicing-tech/" >🔗</a> **[SpaceNews]** Rogue Space Systems gets US Air Force funds to advance in-orbit servicing tech


- <a href="https://www.cnbc.com/2023/09/27/faa-closes-investigation-into-blue-origins-new-shepard-rocket-failure.html" >🔗</a> **[CNBC]** FAA closes investigation into Blue Origin rocket failure, requires 21 ‘corrective actions’


- <a href="https://europeanspaceflight.com/esa-to-publish-vega-c-test-z40-test-failure-findings-this-week/" >🔗</a> **[European Spaceflight]** ESA to Publish Vega C Test Z40 Test Failure Findings This Week


- <a href="http://www.nasa.gov/press-release/regreso-del-astronauta-de-la-NASA-que-batio-records-y-sus-companeros" >🔗</a> **[NASA]** Regreso del astronauta de la NASA que batió récords y sus compañeros


- <a href="http://www.nasa.gov/press-release/record-setting-nasa-astronaut-crewmates-return-from-space-mission" >🔗</a> **[NASA]** Record-Setting NASA Astronaut, Crewmates Return from Space Mission


  - <a href="https://go4liftoff.com/launch/id/bc73ec4f-633e-4eb5-8b8e-5c996ea1733f" >🚀</a> **Soyuz 2.1a | Soyuz MS-22** from Baikonur Cosmodrome, Republic of Kazakhstan

  - <a href="https://go4liftoff.com/launch/id/e3290e0e-d967-4a5d-95eb-f8fae06a9034" >🚀</a> **Soyuz 2.1a | Soyuz MS-23** from Baikonur Cosmodrome, Republic of Kazakhstan



- <a href="https://spacepolicyonline.com/news/frank-rubio-back-on-terra-firma-after-record-setting-371-day-spaceflight/" >🔗</a> **[SpacePolicyOnline.com]** Frank Rubio Back on Terra Firma After Record-Setting 371-Day Spaceflight


  - <a href="https://go4liftoff.com/launch/id/bc73ec4f-633e-4eb5-8b8e-5c996ea1733f" >🚀</a> **Soyuz 2.1a | Soyuz MS-22** from Baikonur Cosmodrome, Republic of Kazakhstan

  - <a href="https://go4liftoff.com/launch/id/e3290e0e-d967-4a5d-95eb-f8fae06a9034" >🚀</a> **Soyuz 2.1a | Soyuz MS-23** from Baikonur Cosmodrome, Republic of Kazakhstan



- <a href="https://spacenews.com/soyuz-returns-iss-crew-after-record-setting-stay/" >🔗</a> **[SpaceNews]** Soyuz returns ISS crew after record-setting stay


  - <a href="https://go4liftoff.com/launch/id/bc73ec4f-633e-4eb5-8b8e-5c996ea1733f" >🚀</a> **Soyuz 2.1a | Soyuz MS-22** from Baikonur Cosmodrome, Republic of Kazakhstan

  - <a href="https://go4liftoff.com/launch/id/e3290e0e-d967-4a5d-95eb-f8fae06a9034" >🚀</a> **Soyuz 2.1a | Soyuz MS-23** from Baikonur Cosmodrome, Republic of Kazakhstan





## Latest Blog Posts 🪧

- <a href="https://europeanspaceflight.substack.com/p/avios-stock-price-takes-a-dive" >🔗</a> **[European Spaceflight]** Avio's stock price takes a dive


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-september-11-24-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: September 11-24, 2023


- <a href="https://www.planetary.org/articles/osiris-rex-returns-sample-to-earth" >🔗</a> **[Planetary Society]** OSIRIS-REx returns sample from asteroid Bennu to Earth


- <a href="https://www.planetary.org/the-downlink/equinox-and-equilux" >🔗</a> **[Planetary Society]** Equinox and equilux


- <a href="https://www.planetary.org/articles/what-is-an-annular-solar-eclipse" >🔗</a> **[Planetary Society]** What is an annular solar eclipse?


- <a href="https://www.planetary.org/articles/the-day-of-action-returns-to-capitol-hill" >🔗</a> **[Planetary Society]** The Day of Action returns to Capitol Hill


- <a href="https://www.planetary.org/articles/tips-for-2024-total-solar-eclipse" >🔗</a> **[Planetary Society]** Want to experience the 2024 total solar eclipse? Here are some tips.


- <a href="https://blog.ulalaunch.com/blog/protoflight-atlas-v-stacked-ahead-of-first-kuiper-launch" >🔗</a> **[United Launch Alliance]** Protoflight: Atlas V stacked ahead of first Kuiper launch


- <a href="https://europeanspaceflight.substack.com/p/is-there-a-future-for-the-european" >🔗</a> **[European Spaceflight]** Is there a future for the European Astronaut Corps?


- <a href="https://www.planetary.org/the-downlink/lost-and-found" >🔗</a> **[Planetary Society]** Lost and found




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230928T071256">2023-09-28 07:12:56 UTC</a>
  <br>
</div>