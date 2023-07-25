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
- <a href="https://www.teslarati.com/spacex-performs-first-fueling-tests-on-super-heavy-booster/" >🔗</a> **[Teslarati]** SpaceX performs first fueling tests on Super Heavy Booster


  - <a href="https://go4liftoff.com/launch/id/04b91bb8-38a7-4868-b025-4bbe05d1fbfe" >🚀</a> **Starship | Integrated Flight Test 2** from SpaceX Space Launch Facility, TX, USA



- <a href="https://spacenews.com/varda-waiting-on-faa-license-to-return-space-manufacturing-capsule/" >🔗</a> **[SpaceNews]** Varda waiting on FAA license to return space manufacturing capsule


  - <a href="https://go4liftoff.com/launch/id/1e0c3a19-02a8-481b-9b7e-1392327c1826" >🚀</a> **Falcon 9 Block 5 | Transporter 8 (Dedicated SSO Rideshare)** from Vandenberg SFB, CA, USA



- <a href="https://spacenews.com/capstone-working-well-more-than-a-year-after-launch/" >🔗</a> **[SpaceNews]** CAPSTONE working well more than a year after launch


  - <a href="https://go4liftoff.com/launch/id/859bf952-b4c6-40fb-a7e7-ac12efc386b2" >🚀</a> **Electron | CAPSTONE** from Onenui Station, Mahia Peninsula, New Zealand



- <a href="https://arstechnica.com/space/2023/07/christmas-is-coming-for-asteroid-scientists-just-2-months-from-today/" >🔗</a> **[Arstechnica]** After bopping an asteroid 3 years ago, NASA will finally see the results


  - <a href="https://go4liftoff.com/launch/id/0bcc6850-4c51-4b08-aa19-0b3753351b9b" >🚀</a> **Atlas V 411 | OSIRIS-REx** from Cape Canaveral, FL, USA




  - <a href="https://go4liftoff.com/event/id/36" >📆</a> **OSIRIS-Rex Sample Return**


- <a href="https://www.teslarati.com/spacex-launches-next-batch-of-starlink-satellites/" >🔗</a> **[Teslarati]** SpaceX launches next batch of Starlink satellites


  - <a href="https://go4liftoff.com/launch/id/c407b340-49e6-447a-b872-8441618f0ec7" >🚀</a> **Falcon 9 Block 5 | Starlink Group 6-6** from Cape Canaveral, FL, USA



- <a href="https://europeanspaceflight.com/maiaspace-reports-expenses-of-e349m-in-its-first-year-of-operation/" >🔗</a> **[European Spaceflight]** MaiaSpace Reports Expenses of €3.49M in its First Year of Operation


- <a href="https://spacenews.com/startup-impulse-space-raises-45-million-in-series-a-round/" >🔗</a> **[SpaceNews]** Startup Impulse Space raises $45 million in Series A round


- <a href="https://spacenews.com/maxar-to-begin-production-of-new-small-satellite-bus/" >🔗</a> **[SpaceNews]** Maxar to begin production of new small satellite bus


- <a href="https://tlpnetwork.com/news/2023/07/nasa_completes_first_artemis_2_launch_simulation" >🔗</a> **[The Launch Pad]** NASA Conducts First Artemis 2 Launch Simulation


  - <a href="https://go4liftoff.com/launch/id/41699701-2ef4-4b0c-ac9d-6757820cde87" >🚀</a> **SLS Block 1 | Artemis II** from Kennedy Space Center, FL, USA



- <a href="https://spacenews.com/chinas-casic-to-begin-launching-vleo-satellites-in-december/" >🔗</a> **[SpaceNews]** China’s CASIC to begin launching VLEO satellites in December




## Latest Blog Posts 🪧

- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-july-17-23-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: July 17-23, 2023


- <a href="https://europeanspaceflight.substack.com/p/how-can-thales-use-space-rider-ip" >🔗</a> **[European Spaceflight]** How can Thales use Space Rider IP for Rev-1?


- <a href="https://www.planetary.org/the-downlink/thats-a-mare" >🔗</a> **[Planetary Society]** That’s a mare


- <a href="https://www.planetary.org/articles/the-senate-threatens-to-cancel-mars-sample-return" >🔗</a> **[Planetary Society]** The U.S. Senate threatens to cancel Mars Sample Return


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-july-3-16-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: July 3-16, 2023


- <a href="https://europeanspaceflight.substack.com/p/a-little-boost-goes-a-long-way" >🔗</a> **[European Spaceflight]** A little Boost! goes a long way


- <a href="https://www.planetary.org/the-downlink/speedy-spacecraft-and-pretty-pics" >🔗</a> **[Planetary Society]** Speedy spacecraft and pretty pics


- <a href="https://www.planetary.org/space-missions/chandrayaan-3" >🔗</a> **[Planetary Society]** Chandrayaan-3, India's Moon lander and rover


- <a href="https://europeanspaceflight.substack.com/p/what-will-become-of-the-german-north" >🔗</a> **[European Spaceflight]** What will become of the German North Sea floating launch site?


- <a href="https://www.planetary.org/advocacy-action-center" >🔗</a> **[Planetary Society]** Advocacy Action Center




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230725T141317">2023-07-25 14:13:17 UTC</a>
  <br>
</div>