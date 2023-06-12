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
- <a href="https://spacenews.com/space-force-sorting-out-complexities-of-wartime-contracting/" >🔗</a> **[SpaceNews]** Space Force sorting out complexities of wartime contracting


- <a href="https://spacenews.com/state-department-framework-seeks-to-coordinate-its-space-policy-activities/" >🔗</a> **[SpaceNews]** State Department framework seeks to coordinate its space policy activities


- <a href="https://www.nasaspaceflight.com/2023/06/grass-update/" >🔗</a> **[NASASpaceflight]** Gravimeter for ESA’s Hera mission is ready to launch to Dimorphos asteroid


  - <a href="https://go4liftoff.com/launch/id/e1ffdd01-c146-44d0-a250-b845dc2eb20d" >🚀</a> **Falcon 9 Block 5 | Hera** from Cape Canaveral, FL, USA



- <a href="https://spacenews.com/should-the-faa-regulate-all-space-activities/" >🔗</a> **[SpaceNews]** Should the FAA regulate all space activities?


- <a href="https://spacenews.com/u-s-space-force-in-talks-with-allies-about-how-to-jointly-protect-space-assets/" >🔗</a> **[SpaceNews]** U.S. Space Force in talks with allies about how to jointly protect space assets


- <a href="https://spacenews.com/house-republicans-introduce-bill-to-create-an-independent-noaa/" >🔗</a> **[SpaceNews]** House Republicans introduce bill to create an independent NOAA


- <a href="https://spacenews.com/ursa-major-confirms-layoffs-necessary-workforce-reductions/" >🔗</a> **[SpaceNews]** Ursa Major confirms layoffs: ‘Necessary workforce reductions’


- <a href="https://spacenews.com/iridium-calls-on-us-to-follow-canadas-ligado-rejection/" >🔗</a> **[SpaceNews]** Iridium calls on US to follow Canada’s Ligado rejection


- <a href="https://spacenews.com/noaa-tracks-smoke-moving-from-the-east-coast-over-the-atlantic/" >🔗</a> **[SpaceNews]** NOAA is tracking smoke moving from the East Coast over the Atlantic


- <a href="https://www.nasaspaceflight.com/2023/06/twis-20230609/" >🔗</a> **[NASASpaceflight]** This Week In Spaceflight: Vulcan fires up, Canadian fires from space, and JWST deep field data


  - <a href="https://go4liftoff.com/launch/id/d0fa4bb2-80ea-4808-af08-7785dde53bf6" >🚀</a> **Ariane 5 ECA+ | James Webb Space Telescope (JWST)** from Kourou, French Guiana




  - <a href="https://go4liftoff.com/event/id/782" >📆</a> **Vulcan Cert-1 Flight Readiness Firing (FRF)**




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/the-downlink/the-scientific-truth-is-out-there" >🔗</a> **[Planetary Society]** The scientific truth is out there


- <a href="https://www.planetary.org/articles/are-aliens-real" >🔗</a> **[Planetary Society]** Are aliens real?


- <a href="https://www.planetary.org/the-downlink/would-you-like-some-salty-water-with-your-space-salad" >🔗</a> **[Planetary Society]** Would you like some salty water with your space salad?


- <a href="https://www.planetary.org/articles/step-grant-winners-2023" >🔗</a> **[Planetary Society]** Space salads and salty waters


- <a href="https://www.planetary.org/the-downlink/way-out-there" >🔗</a> **[Planetary Society]** Way out there


- <a href="https://blog.ulalaunch.com/blog/vulcan-preview-of-the-flight-readiness-firing" >🔗</a> **[United Launch Alliance]** Vulcan: Preview of the Flight Readiness Firing


- <a href="https://www.planetary.org/articles/asteroid-deflection-techniques-to-save-the-earth" >🔗</a> **[Planetary Society]** Five asteroid deflection techniques to save the Earth


- <a href="https://www.planetary.org/the-downlink/moon-spying-missions-and-a-planetary-evil-twin" >🔗</a> **[Planetary Society]** Moon-spying missions and a planetary evil twin


- <a href="https://blog.ulalaunch.com/blog/hypersonic-missiles-are-just-misunderstood" >🔗</a> **[United Launch Alliance]** Hypersonic Missiles are Just Misunderstood


- <a href="https://www.planetary.org/articles/why-is-venus-called-earths-twin" >🔗</a> **[Planetary Society]** Why is Venus called Earth’s twin?




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230612T141305">2023-06-12 14:13:05 UTC</a>
  <br>
</div>