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
- <a href="https://www.teslarati.com/weekly-space-recap-august-28-september-3/" >🔗</a> **[Teslarati]** Weekly Space Recap: August 28 – September 3


- <a href="https://arstechnica.com/space/2023/09/no-firm-date-on-ariane-6s-debut-and-no-public-talk-on-prices-either/" >🔗</a> **[Arstechnica]** European official on Ariane 6 debut: “Please allow me to not speculate at this time”


- <a href="https://spacenews.com/breaking-the-celestial-ceiling/" >🔗</a> **[SpaceNews]** Cracking the celestial ceiling


- <a href="https://www.nasaspaceflight.com/2023/09/nasa-ml-1-artemis-ii-ml-2-construction/" >🔗</a> **[NASASpaceflight]** NASA modifies ML-1 for Artemis II, ML-2 under construction for SLS Block IB


  - <a href="https://go4liftoff.com/launch/id/41699701-2ef4-4b0c-ac9d-6757820cde87" >🚀</a> **SLS Block 1 | Artemis II** from Kennedy Space Center, FL, USA



- <a href="https://spacenews.com/chinese-ceres-1-rocket-reaches-orbit-with-first-sea-launch/" >🔗</a> **[SpaceNews]** Chinese Ceres-1 rocket reaches orbit with first sea launch


  - <a href="https://go4liftoff.com/launch/id/2f255496-16b0-4ae6-ac9e-8e24f5deae7a" >🚀</a> **Ceres-1S | 4x Tianqi** from Sea Launch



- <a href="https://www.teslarati.com/spacex-crew-dragon-crew-6-returns-to-earth-six-months-in-space/" >🔗</a> **[Teslarati]** SpaceX Crew Dragon: Crew 6 returns to Earth after six months in space


  - <a href="https://go4liftoff.com/launch/id/bc325945-4bee-4412-84e1-14998b2eba5f" >🚀</a> **Falcon 9 Block 5 | Crew-6** from Kennedy Space Center, FL, USA




  - <a href="https://go4liftoff.com/event/id/772" >📆</a> **SpaceX Crew-6 Crew Dragon Splashdown**


- <a href="https://www.teslarati.com/spacex-launches-62nd-orbital-mission-of-the-year/" >🔗</a> **[Teslarati]** SpaceX launches 62nd orbital mission of the year


  - <a href="https://go4liftoff.com/launch/id/f66687a3-d1f2-427d-8fe1-0454dc1fe9bd" >🚀</a> **Falcon 9 Block 5 | Starlink Group 6-12** from Kennedy Space Center, FL, USA



- <a href="https://www.nasaspaceflight.com/2023/09/solar-orbiter-picoflare/" >🔗</a> **[NASASpaceflight]** Solar Orbiter discovers plasma jets that could fuel the production of solar wind


  - <a href="https://go4liftoff.com/launch/id/acdd0fab-b485-4c18-bb6f-c45cb62bdfd7" >🚀</a> **Atlas V 411 | Solar Orbiter** from Cape Canaveral, FL, USA



- <a href="https://spacenews.com/esa-to-set-target-for-first-ariane-6-launch-after-upcoming-tests/" >🔗</a> **[SpaceNews]** ESA to set target for first Ariane 6 launch after upcoming tests


- <a href="https://spacenews.com/dod-satellites-in-low-earth-orbit-promise-more-connectivity-for-military-users/" >🔗</a> **[SpaceNews]** DoD satellites in low Earth orbit promise more connectivity for military users




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/articles/osiris-rex-sample-return-what-to-expect" >🔗</a> **[Planetary Society]** OSIRIS-REx sample return: What to expect


- <a href="https://europeanspaceflight.substack.com/p/are-europeans-interested-in-going" >🔗</a> **[European Spaceflight]** Are Europeans interested in going to space?


- <a href="https://www.planetary.org/the-downlink/see-for-yourself" >🔗</a> **[Planetary Society]** See for yourself


- <a href="https://www.planetary.org/articles/your-impact-september-equinox-2023" >🔗</a> **[Planetary Society]** Your impact: September equinox 2023


- <a href="https://www.planetary.org/articles/to-the-moon-together" >🔗</a> **[Planetary Society]** To the moon together


- <a href="https://www.planetary.org/articles/a-lunar-saga" >🔗</a> **[Planetary Society]** A lunar saga


- <a href="https://www.planetary.org/space-missions/change-6-collecting-the-first-lunar-farside-samples" >🔗</a> **[Planetary Society]** Chang'e-6, collecting the first lunar farside samples


- <a href="https://europeanspaceflight.substack.com/p/does-european-sci-comm-suck" >🔗</a> **[European Spaceflight]** Does European Sci-Comm Suck?


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-august-21-27-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: August 21-27, 2023


- <a href="https://blog.ulalaunch.com/blog/rocketstars-a-life-that-spans-the-atlas-v-program" >🔗</a> **[United Launch Alliance]** RocketStars: A life that spans the Atlas V program




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230905T201423">2023-09-05 20:14:23 UTC</a>
  <br>
</div>