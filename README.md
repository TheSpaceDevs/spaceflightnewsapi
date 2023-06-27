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
- <a href="https://www.teslarati.com/spacex-euclid-space-telescope-launch-esa/" >🔗</a> **[Teslarati]** SpaceX to launch the Euclid Space Telescope for the European Space Agency


  - <a href="https://go4liftoff.com/launch/id/49d20d1b-18dd-4da6-a061-eacd0156fcc4" >🚀</a> **Falcon 9 Block 5 | Euclid** from Cape Canaveral, FL, USA



- <a href="https://spacenews.com/d-orbit-wins-contracts-to-test-optical-links-and-fly-mini-space-lab/" >🔗</a> **[SpaceNews]** D-Orbit wins contracts to test optical links and fly mini space lab


- <a href="https://spacenews.com/esa-european-companies-back-zero-debris-agreement/" >🔗</a> **[SpaceNews]** ESA, European companies back “zero debris” agreement


- <a href="https://spacenews.com/ses-bid-for-equal-split-of-c-band-proceeds-back-in-play/" >🔗</a> **[SpaceNews]** SES bid for equal split of C-band proceeds back in play


- <a href="https://www.nasaspaceflight.com/2023/06/launch-roundup-062523/" >🔗</a> **[NASASpaceflight]** Launch Roundup: SpaceX to launch Euclid; Virgin Galactic to fly crewed suborbital mission


  - <a href="https://go4liftoff.com/launch/id/6e5725b3-d0e9-4484-9d79-514fe8b978be" >🚀</a> **Soyuz 2.1b/Fregat-M | Meteor-M No.2-3 and others** from Vostochny Cosmodrome, Siberia, Russian Federation

  - <a href="https://go4liftoff.com/launch/id/6109337b-0ac2-4a89-a5fe-dba37cb107fe" >🚀</a> **SpaceShipTwo | Galactic 01** from Air launch to Suborbital flight

  - <a href="https://go4liftoff.com/launch/id/b8f2e028-285c-457d-b807-a6749cfc3af6" >🚀</a> **Firefly Alpha | FLTA003 (VICTUS NOX)** from Vandenberg SFB, CA, USA

  - <a href="https://go4liftoff.com/launch/id/49d20d1b-18dd-4da6-a061-eacd0156fcc4" >🚀</a> **Falcon 9 Block 5 | Euclid** from Cape Canaveral, FL, USA



- <a href="https://spacenews.com/u-k-joins-u-s-space-commands-commercial-space-tracking-cell/" >🔗</a> **[SpaceNews]** U.K. joins U.S. Space Command’s commercial space-tracking cell


- <a href="https://spacenews.com/agile-raises-13-million-to-expand-production/" >🔗</a> **[SpaceNews]** Agile raises $13 million to expand production


- <a href="http://www.nasa.gov/press-release/nasa-to-provide-coverage-as-dragon-departs-station-with-science" >🔗</a> **[NASA]** NASA to Provide Coverage as Dragon Departs Station with Science


  - <a href="https://go4liftoff.com/launch/id/e53eecd6-184d-440a-955a-70fe0fdccbd6" >🚀</a> **Falcon 9 Block 5 | Dragon CRS-2 SpX-28** from Kennedy Space Center, FL, USA




  - <a href="https://go4liftoff.com/event/id/205" >📆</a> **CRS-21 Dragon Undocking**


- <a href="https://spacenews.com/nasa-identifies-potential-major-cost-growth-in-mars-sample-return/" >🔗</a> **[SpaceNews]** NASA identifies potential major cost growth in Mars Sample Return


- <a href="http://www.nasa.gov/press-release/nasa-to-provide-coverage-for-launch-of-esa-dark-universe-mission" >🔗</a> **[NASA]** NASA to Provide Coverage for Launch of ESA ‘Dark Universe’ Mission




## Latest Blog Posts 🪧

- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-june-19-25-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: June 19-25, 2023


- <a href="https://www.planetary.org/articles/announcing-the-2023-shoemaker-neo-grant-winners" >🔗</a> **[Planetary Society]** Announcing the 2023 Shoemaker NEO grant winners


- <a href="https://europeanspaceflight.substack.com/p/everything-you-need-to-know-about-ddb" >🔗</a> **[European Spaceflight]** Everything you need to know about Themis


- <a href="https://www.planetary.org/the-downlink/rings-and-dings" >🔗</a> **[Planetary Society]** Rings and dings


- <a href="https://blog.ulalaunch.com/blog/united-launch-alliance-successfully-launches-the-penultimate-delta-iv-heavy-rocket" >🔗</a> **[United Launch Alliance]** NROL-68: United Launch Alliance Successfully Launches the Penultimate Delta IV Heavy Rocket


- <a href="https://www.planetary.org/articles/ariel-barreiro-interview" >🔗</a> **[Planetary Society]** Marrying the arts and science in space


- <a href="https://www.planetary.org/articles/citizen-astronomer-asteroid-defender-tips" >🔗</a> **[Planetary Society]** Want to be a citizen astronomer and defend Earth from asteroids? Here are some tips.


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-june-12-19-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: June 12-19, 2023


- <a href="https://europeanspaceflight.substack.com/p/reusability-efforts-of-european-launch" >🔗</a> **[European Spaceflight]** Reusability efforts of European launch startups


- <a href="https://www.planetary.org/the-downlink/day-and-night-its-all-about-starlight" >🔗</a> **[Planetary Society]** Day and night, it’s all about starlight




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230627T101742">2023-06-27 10:17:42 UTC</a>
  <br>
</div>