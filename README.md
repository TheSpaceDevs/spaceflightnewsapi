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
- <a href="https://spacenews.com/ses-qa-leveling-up-multi-orbit-connectivity/" >🔗</a> **[SpaceNews]** SES Q&A | Leveling up multi-orbit connectivity


- <a href="https://spacenews.com/rapid-starlink-iteration-poses-challenges-for-resellers/" >🔗</a> **[SpaceNews]** Rapid Starlink iteration poses challenges for resellers


- <a href="https://europeanspaceflight.com/european-industry-could-generate-e9-9-billion-from-crewed-launch/" >🔗</a> **[European Spaceflight]** European Industry Could Generate €9.9 Billion From Crewed Launch


- <a href="https://spacenews.com/space-force-to-release-guidelines-for-the-use-of-commercial-satellite-services/" >🔗</a> **[SpaceNews]** Space Force to release guidelines for the use of commercial satellite services


- <a href="https://arstechnica.com/space/2023/09/a-nasa-astronaut-will-finally-spend-a-full-year-in-space/" >🔗</a> **[Arstechnica]** A NASA astronaut will finally spend a full year in space


- <a href="https://www.nasaspaceflight.com/2023/09/space-x-wait-faa-approval-starship-flight-two/" >🔗</a> **[NASASpaceflight]** SpaceX waiting for FAA to approve launch licence for Starship’s second flight


- <a href="https://spacenews.com/ula-has-no-issues-with-space-force-plan-to-select-three-national-security-launch-providers/" >🔗</a> **[SpaceNews]** ULA has ‘no issues’ with Space Force plan to select three national security launch providers


- <a href="https://tlpnetwork.com/news/2023/09/nasa-releases-artemis-1-in-flight-anomalies-breakdown" >🔗</a> **[The Launch Pad]** BREAKING! NASA Releases Artemis 1 In Flight Anomalies Breakdown


- <a href="https://www.teslarati.com/spacex-no-longer-losing-money-starlink-antenna-production/" >🔗</a> **[Teslarati]** SpaceX says it is no longer losing money with Starlink production


- <a href="https://www.cnbc.com/2023/09/13/spacex-no-longer-taking-losses-to-produce-starlink-satellite-antennas.html" >🔗</a> **[CNBC]** SpaceX no longer taking losses to produce Starlink antennas, a key step to improving profitability




## Latest Blog Posts 🪧

- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-september-4-10-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: September 4-10, 2023


- <a href="https://www.planetary.org/the-downlink/cometary-sights-and-sounds" >🔗</a> **[Planetary Society]** Cometary sights and sounds


- <a href="https://www.planetary.org/articles/eclipse-2024-checklist" >🔗</a> **[Planetary Society]** A checklist for what to expect during the 2024 total solar eclipse


- <a href="https://www.planetary.org/articles/are-your-solar-eclipse-glasses-safe" >🔗</a> **[Planetary Society]** Are your solar eclipse glasses safe?


- <a href="https://www.planetary.org/articles/how-to-see-newly-discovered-comet-nishimura" >🔗</a> **[Planetary Society]** How to see newly discovered Comet Nishimura


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-august-28-september-3-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: August 28-September 3, 2023


- <a href="https://www.planetary.org/articles/osiris-rex-sample-return-what-to-expect" >🔗</a> **[Planetary Society]** OSIRIS-REx sample return: What to expect


- <a href="https://europeanspaceflight.substack.com/p/are-europeans-interested-in-going" >🔗</a> **[European Spaceflight]** Are Europeans interested in going to space?


- <a href="https://www.planetary.org/the-downlink/see-for-yourself" >🔗</a> **[Planetary Society]** See for yourself


- <a href="https://www.planetary.org/articles/your-impact-september-equinox-2023" >🔗</a> **[Planetary Society]** Your impact: September equinox 2023




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230914T041609">2023-09-14 04:16:09 UTC</a>
  <br>
</div>