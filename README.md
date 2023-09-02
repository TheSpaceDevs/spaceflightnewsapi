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
- <a href="https://www.nasaspaceflight.com/2023/09/india-aditya-l1-pslv/" >🔗</a> **[NASASpaceflight]** India to launch first solar research mission, Aditya-L1, aboard PSLV


- <a href="https://spacepolicyonline.com/news/nasas-lro-spots-likely-luna-25-crash-site/" >🔗</a> **[SpacePolicyOnline.com]** NASA’s LRO Spots Likely Luna-25 Crash Site


- <a href="https://www.nasaspaceflight.com/2023/09/osiris-rex-tests/" >🔗</a> **[NASASpaceflight]** OSIRIS-REx teams conduct final rehearsals before sample capsule return in September


- <a href="https://spacenews.com/ball-northrop-grumman-orbital-micro-systems-and-spire-claim-noaa-contracts/" >🔗</a> **[SpaceNews]** Ball, Northrop Grumman, Orbital Micro Systems and Spire claim NOAA contracts


- <a href="http://www.nasa.gov/press-release/nasa-to-discuss-psyche-asteroid-mission-optical-communications-demo" >🔗</a> **[NASA]** NASA to Discuss Psyche Asteroid Mission, Optical Communications Demo


  - <a href="https://go4liftoff.com/launch/id/66133437-db31-4098-8e3e-cf34c8125f9b" >🚀</a> **Falcon Heavy | Psyche** from Kennedy Space Center, FL, USA



- <a href="https://spacepolicyonline.com/news/sbag-wants-reconnaissance-mission-to-apophis-before-it-reaches-earth/" >🔗</a> **[SpacePolicyOnline.com]** SBAG Wants Reconnaissance Mission to Apophis Before It Reaches Earth


- <a href="https://spacenews.com/space-tango-names-new-ceo/" >🔗</a> **[SpaceNews]** Space Tango names new CEO


- <a href="https://www.cnbc.com/2023/09/01/bezos-snubbed-musk-spacex-satellite-contract-lawsuit.html" >🔗</a> **[CNBC]** Bezos snubbed Musk’s SpaceX over blockbuster satellite launch contract, Amazon shareholder says


- <a href="https://arstechnica.com/space/2023/09/pension-fund-sues-jeff-bezos-and-amazon-for-not-using-falcon-9-rockets/" >🔗</a> **[Arstechnica]** Pension fund sues Jeff Bezos and Amazon for not using Falcon 9 rockets


- <a href="https://europeanspaceflight.com/what-is-the-esa-astronaut-policy/" >🔗</a> **[European Spaceflight]** What is the ESA Astronaut Policy?




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/the-downlink/see-for-yourself" >🔗</a> **[Planetary Society]** See for yourself


- <a href="https://www.planetary.org/articles/your-impact-september-equinox-2023" >🔗</a> **[Planetary Society]** Your impact: September equinox 2023


- <a href="https://www.planetary.org/articles/to-the-moon-together" >🔗</a> **[Planetary Society]** To the moon together


- <a href="https://www.planetary.org/articles/a-lunar-saga" >🔗</a> **[Planetary Society]** A lunar saga


- <a href="https://www.planetary.org/space-missions/change-6-collecting-the-first-lunar-farside-samples" >🔗</a> **[Planetary Society]** Chang'e-6, collecting the first lunar farside samples


- <a href="https://europeanspaceflight.substack.com/p/does-european-sci-comm-suck" >🔗</a> **[European Spaceflight]** Does European Sci-Comm Suck?


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-august-21-27-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: August 21-27, 2023


- <a href="https://blog.ulalaunch.com/blog/rocketstars-a-life-that-spans-the-atlas-v-program" >🔗</a> **[United Launch Alliance]** RocketStars: A life that spans the Atlas V program


- <a href="https://www.planetary.org/the-downlink/moonstruck" >🔗</a> **[Planetary Society]** Moonstruck


- <a href="https://blog.ulalaunch.com/blog/rocketstars-engineer-moves-from-aircraft-to-launching-satellites-at-ula" >🔗</a> **[United Launch Alliance]** RocketStars: Engineer moves from aircraft to launching satellites at ULA




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230902T021619">2023-09-02 02:16:19 UTC</a>
  <br>
</div>