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
- <a href="https://spacenews.com/fixed-price-satellite-contracts-earn-high-grades-in-space-force-report-card/" >🔗</a> **[SpaceNews]** Fixed-price satellite contracts earn high grades in Space Force report card


- <a href="https://spacenews.com/northrop-grumman-gets-80-million-air-force-contract-for-satcom-experiments/" >🔗</a> **[SpaceNews]** Northrop Grumman gets $80 million Air Force contract for satcom experiments


- <a href="https://www.nasa.gov/press-release/nasa-awards-technical-workforce-training-contract" >🔗</a> **[NASA]** NASA Awards Technical Workforce Training Contract


- <a href="https://arstechnica.com/space/2023/06/to-keep-starliner-flying-boeing-must-make-some-hard-choices/" >🔗</a> **[Arstechnica]** To keep Starliner flying, Boeing must make some hard choices


  - <a href="https://go4liftoff.com/launch/id/968067d1-8c12-4018-9854-b7b7d4bddc6b" >🚀</a> **Atlas V N22 | CST-100 Starliner Crewed Flight Test** from Cape Canaveral, FL, USA



- <a href="https://www.nasaspaceflight.com/2023/06/twis-20230602/" >🔗</a> **[NASASpaceflight]** This Week In Spaceflight: China’s lunar plans, North Korea’s failed launch, and Starliner delays


  - <a href="https://go4liftoff.com/launch/id/4aa4088f-4129-4f32-8a89-751f2a54288b" >🚀</a> **Chollima 1 | Malligyong-1** from Sohae Satellite Launching Station,  Cholsan County, North Pyongan Province, Democratic People's Republic of Korea

  - <a href="https://go4liftoff.com/launch/id/968067d1-8c12-4018-9854-b7b7d4bddc6b" >🚀</a> **Atlas V N22 | CST-100 Starliner Crewed Flight Test** from Cape Canaveral, FL, USA



- <a href="https://spacenews.com/space-comm-expo-2023-where-space-does-business/" >🔗</a> **[SpaceNews]** Space-Comm Expo 2023 – Where Space Does Business


- <a href="https://spacenews.com/google-leads-36-million-funding-round-for-pixxel/" >🔗</a> **[SpaceNews]** Google leads $36 million funding round for Pixxel


- <a href="https://arstechnica.com/space/2023/06/rocket-report-spacex-pushing-ahead-on-starbase-north-korea-launch-failure/" >🔗</a> **[Arstechnica]** Rocket Report: SpaceX pushing ahead on Starbase, North Korea launch failure


  - <a href="https://go4liftoff.com/launch/id/4aa4088f-4129-4f32-8a89-751f2a54288b" >🚀</a> **Chollima 1 | Malligyong-1** from Sohae Satellite Launching Station,  Cholsan County, North Pyongan Province, Democratic People's Republic of Korea



- <a href="https://spacenews.com/parachute-and-wiring-issues-to-delay-starliner-crewed-test-flight/" >🔗</a> **[SpaceNews]** Parachute and wiring issues to delay Starliner crewed test flight


  - <a href="https://go4liftoff.com/launch/id/968067d1-8c12-4018-9854-b7b7d4bddc6b" >🚀</a> **Atlas V N22 | CST-100 Starliner Crewed Flight Test** from Cape Canaveral, FL, USA



- <a href="http://www.nasa.gov/press-release/nasa-invites-public-to-sign-poem-that-will-fly-aboard-europa-clipper" >🔗</a> **[NASA]** NASA Invites Public to Sign Poem That Will Fly Aboard Europa Clipper


  - <a href="https://go4liftoff.com/launch/id/59548105-347d-4477-8747-7fc3f91016c5" >🚀</a> **Falcon Heavy | Europa Clipper** from Kennedy Space Center, FL, USA





## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/the-downlink/would-you-like-some-salty-water-with-your-space-salad" >🔗</a> **[Planetary Society]** Would you like some salty water with your space salad?


- <a href="https://www.planetary.org/articles/step-grant-winners-2023" >🔗</a> **[Planetary Society]** Space salads and salty waters


- <a href="https://www.planetary.org/the-downlink/way-out-there" >🔗</a> **[Planetary Society]** Way out there


- <a href="https://blog.ulalaunch.com/blog/vulcan-preview-of-the-flight-readiness-firing" >🔗</a> **[United Launch Alliance]** Vulcan: Preview of the Flight Readiness Firing


- <a href="https://www.planetary.org/articles/asteroid-deflection-techniques-to-save-the-earth" >🔗</a> **[Planetary Society]** Five asteroid deflection techniques to save the Earth


- <a href="https://www.planetary.org/the-downlink/moon-spying-missions-and-a-planetary-evil-twin" >🔗</a> **[Planetary Society]** Moon-spying missions and a planetary evil twin


- <a href="https://blog.ulalaunch.com/blog/hypersonic-missiles-are-just-misunderstood" >🔗</a> **[United Launch Alliance]** Hypersonic Missiles are Just Misunderstood


- <a href="https://www.planetary.org/articles/why-is-venus-called-earths-twin" >🔗</a> **[Planetary Society]** Why is Venus called Earth’s twin?


- <a href="https://www.planetary.org/the-downlink/hard-working-spacecraft-and-even-harder-working-microbes" >🔗</a> **[Planetary Society]** Hard-working spacecraft and even harder-working microbes


- <a href="https://www.planetary.org/articles/why-has-spacexs-starship-sparked-an-environmental-controversy" >🔗</a> **[Planetary Society]** Why has SpaceX's Starship sparked an environmental controversy?




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230603T161748">2023-06-03 16:17:48 UTC</a>
  <br>
</div>