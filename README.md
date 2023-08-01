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
- <a href="https://spacenews.com/astro-digital-to-integrate-astroscale-in-orbit-servicing-docking-plates/" >🔗</a> **[SpaceNews]** Astro Digital to integrate Astroscale in-orbit servicing docking plates


- <a href="https://www.teslarati.com/northrup-grumman-antares-swan-song-launch/" >🔗</a> **[Teslarati]** Northrup Grumman’s Antares set for its swan song launch


- <a href="https://www.nasaspaceflight.com/2023/08/antares-230-farewell-launch/" >🔗</a> **[NASASpaceflight]** Antares 230+ farewell launch to fly S.S. Laurel Clark to ISS


  - <a href="https://go4liftoff.com/launch/id/7c126e4f-4afd-4c25-bf6f-9017666b56ee" >🚀</a> **Antares 230+ | Cygnus CRS-2 NG-19** from Wallops Island, Virginia, USA



- <a href="https://tlpnetwork.com/news/2023/08/antares_launches_final_russian_parts_configuration" >🔗</a> **[The Launch Pad]** Antares prepares to fly its last mission using Russian and Ukrainian parts


  - <a href="https://go4liftoff.com/launch/id/7c126e4f-4afd-4c25-bf6f-9017666b56ee" >🚀</a> **Antares 230+ | Cygnus CRS-2 NG-19** from Wallops Island, Virginia, USA



- <a href="https://spacenews.com/senate-committee-advances-orbital-debris-removal-bill/" >🔗</a> **[SpaceNews]** Senate committee advances orbital debris removal bill


- <a href="https://www.cnbc.com/2023/08/01/planet-pl-lays-off-about-10percent-company-restructures.html" >🔗</a> **[CNBC]** Planet lays off about 10% of workforce as satellite imagery company restructures


- <a href="https://www.teslarati.com/rocket-labs-electron-faces-rare-last-second-abort/" >🔗</a> **[Teslarati]** Rocket Lab’s Electron faces rare last second abort


  - <a href="https://go4liftoff.com/launch/id/7975274c-81c5-48a5-82e1-9b8d982cd533" >🚀</a> **Electron | We Love the Nightlife (Capella Acadia 1)** from Onenui Station, Mahia Peninsula, New Zealand



- <a href="https://spacenews.com/u-s-space-command-headquarters-to-remain-in-colorado/" >🔗</a> **[SpaceNews]** U.S. Space Command headquarters to remain in Colorado


- <a href="https://www.nasaspaceflight.com/2023/07/launch-roundup-spacex-galaxy-37-china-fy-3f/" >🔗</a> **[NASASpaceflight]** Launch Roundup: SpaceX to launch Galaxy 37; China to launch FY-3F


  - <a href="https://go4liftoff.com/launch/id/5749ccdb-a743-49e9-b7d0-3c018dc68ae3" >🚀</a> **Long March 4C | Fengyun-3F** from Jiuquan Satellite Launch Center, People's Republic of China

  - <a href="https://go4liftoff.com/launch/id/afc772a3-6ea7-4550-a4e9-35c70c22ebba" >🚀</a> **Falcon 9 Block 5 | Galaxy 37** from Cape Canaveral, FL, USA



- <a href="http://www.nasa.gov/press-release/nasa-boeing-to-provide-progress-update-on-starliner-crew-flight-test" >🔗</a> **[NASA]** NASA, Boeing to Provide Progress Update on Starliner Crew Flight Test



  - <a href="https://go4liftoff.com/event/id/841" >📆</a> **Boeing Starliner CFT Media Teleconference**




## Latest Blog Posts 🪧

- <a href="https://europeanspaceflight.substack.com/p/will-esa-finally-land-on-mars" >🔗</a> **[European Spaceflight]** Will ESA finally land on Mars?


- <a href="https://www.planetary.org/the-downlink/aquatic-equivalencies" >🔗</a> **[Planetary Society]** Aquatic equivalencies


- <a href="https://www.planetary.org/articles/life-on-venus-your-questions-answered" >🔗</a> **[Planetary Society]** Life on Venus: Your Questions Answered


- <a href="https://europeanspaceflight.substack.com/p/the-time-europe-tried-to-copy-energia" >🔗</a> **[European Spaceflight]** The time Europe tried to copy Energia


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-july-17-23-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: July 17-23, 2023


- <a href="https://europeanspaceflight.substack.com/p/how-can-thales-use-space-rider-ip" >🔗</a> **[European Spaceflight]** How can Thales use Space Rider IP for Rev-1?


- <a href="https://www.planetary.org/the-downlink/thats-a-mare" >🔗</a> **[Planetary Society]** That’s a mare


- <a href="https://www.planetary.org/articles/the-senate-threatens-to-cancel-mars-sample-return" >🔗</a> **[Planetary Society]** The U.S. Senate threatens to cancel Mars Sample Return


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-july-3-16-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: July 3-16, 2023


- <a href="https://europeanspaceflight.substack.com/p/a-little-boost-goes-a-long-way" >🔗</a> **[European Spaceflight]** A little Boost! goes a long way




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230801T181713">2023-08-01 18:17:13 UTC</a>
  <br>
</div>