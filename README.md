![Cover](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/snapi_poster.png)

[![Website](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/badge_snapi_website.svg)](https://spaceflightnewsapi.net/)
[![Documentation](https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/badge_snapi_doc.svg)](https://api.spaceflightnewsapi.net/v4/docs)
[![Version](https://img.shields.io/github/v/release/TheSpaceDevs/spaceflightnewsapi?style=for-the-badge)](https://github.com/TheSpaceDevs/spaceflightnewsapi/releases/tag/v4.0.1)
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

- TechCrunch
- SpaceFlight Insider
- SpaceX
- ElonX
- Blue Origin
- Spaceflight Now
- Space.com
- Teslarati
- Virgin Galactic
- Planetary Society
- Phys
- National Space Society
- The Japan Times
- National Geographic
- SpaceNews
- The National
- Jet Propulsion Laboratory
- NASA
- The Space Review
- The Verge
- The Drive
- Arstechnica
- ESA
- The Space Devs
- AmericaSpace
- The Wall Street Journal
- CNBC
- United Launch Alliance
- Reuters
- The New York Times
- euronews
- European Spaceflight Update
- NASASpaceflight
- SyFy
- The Launch Pad


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



## Latest News Articles ⌛
- <a href="http://www.nasa.gov/press-release/axiom-space-private-astronauts-headed-to-international-space-station" >🔗</a> **[NASA]** Axiom Space Private Astronauts Headed to International Space Station


  - <a href="https://go4liftoff.com/launch/id/0297d3dc-0513-450a-babc-6f3da8e8c181" >🚀</a> **Falcon 9 Block 5 | Axiom Space Mission 2** from Kennedy Space Center, FL, USA



- <a href="https://spacenews.com/spacex-launches-second-axiom-space-private-astronaut-mission-to-iss/" >🔗</a> **[SpaceNews]** SpaceX launches second Axiom Space private astronaut mission to ISS


  - <a href="https://go4liftoff.com/launch/id/0297d3dc-0513-450a-babc-6f3da8e8c181" >🚀</a> **Falcon 9 Block 5 | Axiom Space Mission 2** from Kennedy Space Center, FL, USA



- <a href="https://spacenews.com/nasa-seeks-to-shore-up-congressional-support-for-artemis/" >🔗</a> **[SpaceNews]** NASA seeks to shore up congressional support for Artemis


- <a href="https://spacenews.com/earthdaily-analytics-offers-ven%c2%b5s-imagery-access/" >🔗</a> **[SpaceNews]** EarthDaily Analytics offers VENµS imagery access


- <a href="https://spacenews.com/iceye-to-develop-sar-constellation-for-uae/" >🔗</a> **[SpaceNews]** Iceye to supply UAE SAR satellites


- <a href="https://spacenews.com/planet-seeks-partners-that-can-extract-more-value-from-data/" >🔗</a> **[SpaceNews]** Planet seeks partners that can extract more value from data


- <a href="https://spacenews.com/umbra-and-ursa-to-collaborate-on-radar-imaging-data-products/" >🔗</a> **[SpaceNews]** Umbra and Ursa to collaborate on radar imaging data products


- <a href="https://www.nasaspaceflight.com/2023/05/axiom-2-mission/" >🔗</a> **[NASASpaceflight]** SpaceX launches Axiom-2, carrying four astronauts to the ISS


  - <a href="https://go4liftoff.com/launch/id/0297d3dc-0513-450a-babc-6f3da8e8c181" >🚀</a> **Falcon 9 Block 5 | Axiom Space Mission 2** from Kennedy Space Center, FL, USA



- <a href="https://www.teslarati.com/axiom-2-mission-heads-to-iss-spacex/" >🔗</a> **[Teslarati]** The Axiom-2 mission heads to the International Space Station courtesy of SpaceX


  - <a href="https://go4liftoff.com/launch/id/0297d3dc-0513-450a-babc-6f3da8e8c181" >🚀</a> **Falcon 9 Block 5 | Axiom Space Mission 2** from Kennedy Space Center, FL, USA



- <a href="https://spacenews.com/agencies-studying-safety-issues-of-lox-methane-launch-vehicles/" >🔗</a> **[SpaceNews]** Agencies studying safety issues of LOX/methane launch vehicles




## Latest Blog Posts 🚀

- <a href="https://www.planetary.org/the-downlink/moon-spying-missions-and-a-planetary-evil-twin" >🔗</a> **[Planetary Society]** Moon-spying missions and a planetary evil twin


- <a href="https://blog.ulalaunch.com/blog/hypersonic-missiles-are-just-misunderstood" >🔗</a> **[United Launch Alliance]** Hypersonic Missiles are Just Misunderstood


- <a href="https://www.planetary.org/articles/why-is-venus-called-earths-twin" >🔗</a> **[Planetary Society]** Why is Venus called Earth’s twin?


- <a href="https://www.planetary.org/the-downlink/hard-working-spacecraft-and-even-harder-working-microbes" >🔗</a> **[Planetary Society]** Hard-working spacecraft and even harder-working microbes


- <a href="https://www.planetary.org/articles/why-has-spacexs-starship-sparked-an-environmental-controversy" >🔗</a> **[Planetary Society]** Why has SpaceX's Starship sparked an environmental controversy?


- <a href="https://www.planetary.org/articles/how-did-earth-get-its-oxygen" >🔗</a> **[Planetary Society]** How did Earth get its oxygen?


- <a href="https://www.planetary.org/careers/freelance-digital-advertising-specialist-contract-part-time" >🔗</a> **[Planetary Society]** Freelance Digital Advertising Specialist (Contract & Part-time)


- <a href="https://www.planetary.org/the-downlink/moonshadow-moonshadow" >🔗</a> **[Planetary Society]** Moonshadow, Moonshadow


- <a href="https://blog.ulalaunch.com/blog/why-is-stem-education-a-national-imperative" >🔗</a> **[United Launch Alliance]** Why is STEM Education a National Imperative and How Are We Wasting Our Precious Human Resource?


- <a href="https://www.planetary.org/articles/what-happened-with-psyche" >🔗</a> **[Planetary Society]** What happened with Psyche?




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230522T070733">2023-05-22 07:07:33 UTC</a>
  <br>
</div>