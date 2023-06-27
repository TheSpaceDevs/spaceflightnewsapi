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
- <a href="https://spacenews.com/pld-space-postpones-first-launch-to-september/" >🔗</a> **[SpaceNews]** PLD Space postpones first launch to September


- <a href="https://spacenews.com/house-appropriators-target-space-force-programs/" >🔗</a> **[SpaceNews]** House appropriators target Space Force programs


- <a href="https://spacenews.com/airmo-raises-5-2-million-euros-for-climate-monitoring-constellation/" >🔗</a> **[SpaceNews]** Airmo raises 5.2 million euros for climate-monitoring constellation


- <a href="https://spacenews.com/spacenews-ceo/" >🔗</a> **[SpaceNews]** SpaceNews names new CEO Andrew Pemberton


- <a href="https://tlpnetwork.com/news/2023/06/dorbit-wins-italian-contracts-to-fly-mini-space-lab-and-test-optical-intersatellite-links" >🔗</a> **[The Launch Pad]** D-Orbit Wins Italian Contracts To Fly Mini Space Lab And Test Optical Intersatellite Links


- <a href="https://tlpnetwork.com/news/2023/06/nasa_begins_simulated_mars_mission" >🔗</a> **[The Launch Pad]** NASA begins CHAPEA 1 Mission to "Mars" in Houston


- <a href="https://tlpnetwork.com/news/2023/06/esa-and-european-companies-agree-to-2030-zero-debris-agreement" >🔗</a> **[The Launch Pad]** ESA & European Companies Agree To 2030 "Zero Debris" Agreement


- <a href="https://tlpnetwork.com/news/2023/06/uk-to-form-commercial-space-tracking-cell-partners-with-us-space-command" >🔗</a> **[The Launch Pad]** UK To Form Commercial Space Tracking Cell, Partners With U.S. Space Command's


- <a href="https://www.teslarati.com/spacex-euclid-space-telescope-launch-esa/" >🔗</a> **[Teslarati]** SpaceX to launch the Euclid Space Telescope for the European Space Agency


  - <a href="https://go4liftoff.com/launch/id/49d20d1b-18dd-4da6-a061-eacd0156fcc4" >🚀</a> **Falcon 9 Block 5 | Euclid** from Cape Canaveral, FL, USA



- <a href="https://spacenews.com/d-orbit-wins-contracts-to-test-optical-links-and-fly-mini-space-lab/" >🔗</a> **[SpaceNews]** D-Orbit wins contracts to test optical links and fly mini space lab




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/articles/whats-going-on-with-mars-sample-return" >🔗</a> **[Planetary Society]** What’s going on with Mars Sample Return?


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-june-19-25-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: June 19-25, 2023


- <a href="https://www.planetary.org/articles/announcing-the-2023-shoemaker-neo-grant-winners" >🔗</a> **[Planetary Society]** Announcing the 2023 Shoemaker NEO grant winners


- <a href="https://europeanspaceflight.substack.com/p/everything-you-need-to-know-about-ddb" >🔗</a> **[European Spaceflight]** Everything you need to know about Themis


- <a href="https://www.planetary.org/the-downlink/rings-and-dings" >🔗</a> **[Planetary Society]** Rings and dings


- <a href="https://blog.ulalaunch.com/blog/united-launch-alliance-successfully-launches-the-penultimate-delta-iv-heavy-rocket" >🔗</a> **[United Launch Alliance]** NROL-68: United Launch Alliance Successfully Launches the Penultimate Delta IV Heavy Rocket


- <a href="https://www.planetary.org/articles/ariel-barreiro-interview" >🔗</a> **[Planetary Society]** Marrying the arts and science in space


- <a href="https://www.planetary.org/articles/citizen-astronomer-asteroid-defender-tips" >🔗</a> **[Planetary Society]** Want to be a citizen astronomer and defend Earth from asteroids? Here are some tips.


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-june-12-19-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: June 12-19, 2023


- <a href="https://europeanspaceflight.substack.com/p/reusability-efforts-of-european-launch" >🔗</a> **[European Spaceflight]** Reusability efforts of European launch startups




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230627T201645">2023-06-27 20:16:45 UTC</a>
  <br>
</div>