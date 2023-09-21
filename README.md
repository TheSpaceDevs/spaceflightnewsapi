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
- <a href="https://tlpnetwork.com/news/2023/09/rfa-argo" >🔗</a> **[The Launch Pad]** RFA Submits Argo Spacecraft to ESA Commercial Cargo Transportation Initiative


- <a href="https://mars.nasa.gov/news/9483/" >🔗</a> **[NASA]** NASA Releases Independent Review's Mars Sample Return Report


- <a href="https://www.cnbc.com/2023/09/21/investing-in-space-fireflys-space-force-launch-represents-key-moment.html" >🔗</a> **[CNBC]** Investing in Space: Firefly’s successful launch represents a key moment for company’s future


  - <a href="https://go4liftoff.com/launch/id/b8f2e028-285c-457d-b807-a6749cfc3af6" >🚀</a> **Firefly Alpha | FLTA003 (VICTUS NOX)** from Vandenberg SFB, CA, USA



- <a href="https://spacepolicyonline.com/news/rubio-hits-365-day-mark-in-space-eager-to-get-home/" >🔗</a> **[SpacePolicyOnline.com]** Rubio Hits 365-Day Mark in Space, Eager to Get Home


  - <a href="https://go4liftoff.com/launch/id/bc73ec4f-633e-4eb5-8b8e-5c996ea1733f" >🚀</a> **Soyuz 2.1a | Soyuz MS-22** from Baikonur Cosmodrome, Republic of Kazakhstan

  - <a href="https://go4liftoff.com/launch/id/e3290e0e-d967-4a5d-95eb-f8fae06a9034" >🚀</a> **Soyuz 2.1a | Soyuz MS-23** from Baikonur Cosmodrome, Republic of Kazakhstan



- <a href="https://tlpnetwork.com/news/2023/09/ariane-6-long-duration-hot-fire-delayed-following-anomaly" >🔗</a> **[The Launch Pad]** Ariane 6 Long Duration Hot Fire Delayed Following Anomaly


  - <a href="https://go4liftoff.com/launch/id/3e461ec0-8b64-4804-b9aa-e1e1f066065a" >🚀</a> **Ariane 62 | Maiden Flight** from Kourou, French Guiana




  - <a href="https://go4liftoff.com/event/id/864" >📆</a> **Ariane 6 Full-Duration Static Fire**


- <a href="https://mars.nasa.gov/news/9482/" >🔗</a> **[NASA]** Autonomous Systems Help NASA's Perseverance Do More Science on Mars


  - <a href="https://go4liftoff.com/launch/id/c4db6995-f25f-4608-8eb9-ce95d5226af2" >🚀</a> **Atlas V 541 | Mars 2020 (Perseverance rover & Ingenuity helicopter)** from Cape Canaveral, FL, USA



- <a href="https://europeanspaceflight.com/arianegroup-invests-e27m-more-into-maiaspace/" >🔗</a> **[European Spaceflight]** ArianeGroup Invests €27M More into MaiaSpace


- <a href="https://spacenews.com/the-artemis-accords-changing-the-narrative-from-space-race-to-space-cooperation/" >🔗</a> **[SpaceNews]** The Artemis Accords: Changing the Narrative from Space Race to Space Cooperation


- <a href="https://spacenews.com/chinas-galactic-energy-suffers-first-launch-failure/" >🔗</a> **[SpaceNews]** China’s Galactic Energy suffers first launch failure


- <a href="https://spacenews.com/faa-proposes-rule-to-limit-lifetime-of-upper-stages-in-orbit/" >🔗</a> **[SpaceNews]** FAA proposes rule to limit lifetime of upper stages in orbit




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/articles/the-day-of-action-returns-to-capitol-hill" >🔗</a> **[Planetary Society]** The Day of Action returns to Capitol Hill


- <a href="https://www.planetary.org/articles/tips-for-2024-total-solar-eclipse" >🔗</a> **[Planetary Society]** Want to experience the 2024 total solar eclipse? Here are some tips.


- <a href="https://blog.ulalaunch.com/blog/protoflight-atlas-v-stacked-ahead-of-first-kuiper-launch" >🔗</a> **[United Launch Alliance]** Protoflight: Atlas V stacked ahead of first Kuiper launch


- <a href="https://europeanspaceflight.substack.com/p/is-there-a-future-for-the-european" >🔗</a> **[European Spaceflight]** Is there a future for the European Astronaut Corps?


- <a href="https://www.planetary.org/the-downlink/lost-and-found" >🔗</a> **[Planetary Society]** Lost and found


- <a href="https://www.planetary.org/articles/guide-to-eclipse-vocabulary" >🔗</a> **[Planetary Society]** A guide to eclipse vocabulary


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-september-4-10-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: September 4-10, 2023


- <a href="https://www.planetary.org/the-downlink/cometary-sights-and-sounds" >🔗</a> **[Planetary Society]** Cometary sights and sounds


- <a href="https://www.planetary.org/articles/eclipse-2024-checklist" >🔗</a> **[Planetary Society]** A checklist for what to expect during the 2024 total solar eclipse


- <a href="https://www.planetary.org/articles/are-your-solar-eclipse-glasses-safe" >🔗</a> **[Planetary Society]** Are your solar eclipse glasses safe?




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230921T191054">2023-09-21 19:10:54 UTC</a>
  <br>
</div>