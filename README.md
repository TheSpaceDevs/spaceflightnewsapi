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
- <a href="https://spacepolicyonline.com/news/fcc-nominees-win-committee-approval/" >🔗</a> **[SpacePolicyOnline.com]** FCC Nominees Win Committee Approval


- <a href="https://spacepolicyonline.com/news/stunning-image-crowns-jwsts-first-anniversary/" >🔗</a> **[SpacePolicyOnline.com]** Stunning Image Crowns JWST’s First Anniversary


  - <a href="https://go4liftoff.com/launch/id/d0fa4bb2-80ea-4808-af08-7785dde53bf6" >🚀</a> **Ariane 5 ECA+ | James Webb Space Telescope (JWST)** from Kourou, French Guiana



- <a href="https://www.cnbc.com/2023/07/12/viasat-stock-drops-after-satellite-malfunction.html" >🔗</a> **[CNBC]** Viasat stock plunges after company discloses malfunction in new satellite


  - <a href="https://go4liftoff.com/launch/id/8b1067dd-81c6-4bc3-b0f1-45f78963716f" >🚀</a> **Falcon Heavy | ViaSat-3 Americas & Others** from Kennedy Space Center, FL, USA



- <a href="https://tlpnetwork.com/news/2023/07/viasat-3-deployment-issues" >🔗</a> **[The Launch Pad]** Viasat-3 Experiencing Potentially Fatal Deployment Issues


  - <a href="https://go4liftoff.com/launch/id/8b1067dd-81c6-4bc3-b0f1-45f78963716f" >🚀</a> **Falcon Heavy | ViaSat-3 Americas & Others** from Kennedy Space Center, FL, USA



- <a href="https://www.nasaspaceflight.com/2023/07/jwst-1year/" >🔗</a> **[NASASpaceflight]** One year into science operations, Webb continues to rewrite the textbooks of science


  - <a href="https://go4liftoff.com/launch/id/d0fa4bb2-80ea-4808-af08-7785dde53bf6" >🚀</a> **Ariane 5 ECA+ | James Webb Space Telescope (JWST)** from Kourou, French Guiana



- <a href="https://spacenews.com/biden-nominates-space-force-generals-for-promotion/" >🔗</a> **[SpaceNews]** Biden nominates Space Force generals for promotion


- <a href="https://tlpnetwork.com/news/2023/07/israeli_lunar_lander_facing_funding_woes" >🔗</a> **[The Launch Pad]** Israeli Lunar Landing Mission Struggles with Funding


- <a href="http://www.nasa.gov/press-release/nasa-sets-briefings-for-next-international-space-station-crew-missions" >🔗</a> **[NASA]** NASA Sets Briefings for Next International Space Station Crew Missions


  - <a href="https://go4liftoff.com/launch/id/1caacff9-837e-493b-afd4-4da54eeccdf2" >🚀</a> **Falcon 9 Block 5 | Crew-7** from Kennedy Space Center, FL, USA



- <a href="https://arstechnica.com/space/2023/07/the-webb-telescope-just-offered-a-revelatory-view-of-humanitys-distant-past/" >🔗</a> **[Arstechnica]** The Webb telescope just offered a revelatory view of humanity’s distant past


  - <a href="https://go4liftoff.com/launch/id/d0fa4bb2-80ea-4808-af08-7785dde53bf6" >🚀</a> **Ariane 5 ECA+ | James Webb Space Telescope (JWST)** from Kourou, French Guiana



- <a href="https://tlpnetwork.com/news/2023/07/webb_first_anniversary_spots_stellar_nursery" >🔗</a> **[The Launch Pad]** Webb Celebrates First Anniversary with Stellar Nursery


  - <a href="https://go4liftoff.com/launch/id/d0fa4bb2-80ea-4808-af08-7785dde53bf6" >🚀</a> **Ariane 5 ECA+ | James Webb Space Telescope (JWST)** from Kourou, French Guiana





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
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230713T101652">2023-07-13 10:16:52 UTC</a>
  <br>
</div>