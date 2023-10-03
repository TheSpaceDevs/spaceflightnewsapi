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
- <a href="https://spacenews.com/fcc-fines-dish-network-for-botched-satellite-de-orbit/" >🔗</a> **[SpaceNews]** FCC fines Dish Network for botched satellite de-orbit


- <a href="https://spacenews.com/china-outlines-change-8-resource-utilization-mission-to-the-lunar-south-pole/" >🔗</a> **[SpaceNews]** China outlines Chang’e-8 resource utilization mission to the lunar south pole


- <a href="https://spacenews.com/spacenews-announces-promotion-of-kamal-flucker-to-global-sales-director/" >🔗</a> **[SpaceNews]** SpaceNews Announces Promotion of Kamal Flucker to Global Sales Director


- <a href="https://www.cnbc.com/2023/10/02/fcc-enforces-first-space-debris-penalty-in-dish-network-settlement.html" >🔗</a> **[CNBC]** FCC enforces first space debris penalty in $150,000 settlement with Dish


- <a href="https://spacenews.com/space-force-goal-of-a-multi-vendor-space-network-called-impractical/" >🔗</a> **[SpaceNews]** Space Force goal of a multi-vendor space network called impractical


- <a href="https://arstechnica.com/space/2023/10/northrop-grumman-likely-to-end-its-bid-for-a-commercial-space-station/" >🔗</a> **[Arstechnica]** Northrop Grumman likely to end its bid for a commercial space station


- <a href="https://spacenews.com/heads-of-agencies-update-on-crewed-robotic-lunar-plans/" >🔗</a> **[SpaceNews]** Heads of agencies update on crewed, robotic lunar plans


- <a href="https://spacenews.com/esa-delays-vega-c-return-to-flight-to-late-2024/" >🔗</a> **[SpaceNews]** ESA delays Vega C return to flight to late 2024


- <a href="https://europeanspaceflight.com/vega-c-nozzle-design-to-blame-for-zefiro-40-test-failure/" >🔗</a> **[European Spaceflight]** Vega C Nozzle Design to Blame for Zefiro 40 Test Failure


- <a href="https://www.nasaspaceflight.com/2023/10/saturn-rings/" >🔗</a> **[NASASpaceflight]** New research provides explanation for the origin of Saturn’s rings and icy moons




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/articles/psyche-launch-what-to-expect" >🔗</a> **[Planetary Society]** The Psyche launch and its journey to a metal world: What to expect


- <a href="https://www.planetary.org/the-downlink/with-an-eye-to-the-future" >🔗</a> **[Planetary Society]** With an eye to the future


- <a href="https://blog.ulalaunch.com/blog/protoflight-project-kuiper-payload-placed-atop-atlas-v" >🔗</a> **[United Launch Alliance]** Protoflight: Project Kuiper payload placed atop Atlas V


- <a href="https://www.planetary.org/articles/mike-puzio-bennu-interview" >🔗</a> **[Planetary Society]** The boy who named Bennu is now an aspiring astronaut


- <a href="https://www.planetary.org/articles/why-partial-eclipses-are-worth-seeing" >🔗</a> **[Planetary Society]** Why partial eclipses are worth seeing


- <a href="https://europeanspaceflight.substack.com/p/avios-stock-price-takes-a-dive" >🔗</a> **[European Spaceflight]** Avio's stock price takes a dive


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-september-11-24-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: September 11-24, 2023


- <a href="https://www.planetary.org/articles/osiris-rex-returns-sample-to-earth" >🔗</a> **[Planetary Society]** OSIRIS-REx returns sample from asteroid Bennu to Earth


- <a href="https://www.planetary.org/the-downlink/equinox-and-equilux" >🔗</a> **[Planetary Society]** Equinox and equilux


- <a href="https://www.planetary.org/articles/what-is-an-annular-solar-eclipse" >🔗</a> **[Planetary Society]** What is an annular solar eclipse?




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20231003T022046">2023-10-03 02:20:46 UTC</a>
  <br>
</div>