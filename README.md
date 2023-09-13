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
- <a href="https://spacepolicyonline.com/news/nasas-severely-underfunded-biological-and-physical-sciences-research-program-needs-tenfold-increase/" >🔗</a> **[SpacePolicyOnline.com]** NASA’s “Severely Underfunded” Biological and Physical Sciences Research Program Needs Tenfold Increase


- <a href="https://spacenews.com/kuiper-launch-companies-say-they-can-meet-amazons-schedule/" >🔗</a> **[SpaceNews]** Kuiper launch companies say they can meet Amazon’s schedule


- <a href="https://spacenews.com/space-force-to-create-integrated-units-responsible-for-acquisition-maintenance-and-operations/" >🔗</a> **[SpaceNews]** Space Force to create “integrated” units responsible for acquisition, maintenance and operations


- <a href="https://spacenews.com/phase-four-demonstrates-maxwell-block-2-thruster-in-orbit/" >🔗</a> **[SpaceNews]** Phase Four demonstrates Maxwell Block 2 thruster in orbit


- <a href="https://spacenews.com/intelsat-plotting-a-meo-constellation-in-2027-with-c-band-windfall/" >🔗</a> **[SpaceNews]** Intelsat plotting a MEO constellation in 2027 with C-band windfall


- <a href="https://tlpnetwork.com/news/2023/09/ax3-crew" >🔗</a> **[The Launch Pad]** Axiom Space Announces International Crew Of Axiom 3 Mission


  - <a href="https://go4liftoff.com/launch/id/da48063e-b50f-4602-adab-ad7331ee6d82" >🚀</a> **Falcon 9 Block 5 | Axiom Space Mission 3** from Kennedy Space Center, FL, USA



- <a href="http://www.nasa.gov/press-release/nasa-sets-coverage-for-launch-docking-of-new-space-station-crew" >🔗</a> **[NASA]** NASA Sets Coverage for Launch, Docking of New Space Station Crew


  - <a href="https://go4liftoff.com/launch/id/2a052554-35be-4e6c-8d60-b2b9072de17c" >🚀</a> **Soyuz 2.1a | Soyuz MS-24** from Baikonur Cosmodrome, Republic of Kazakhstan




  - <a href="https://go4liftoff.com/event/id/773" >📆</a> **Soyuz MS-24 Docking**


- <a href="http://www.nasa.gov/press-release/nasa-partners-clear-axiom-space-s-third-private-astronaut-crew" >🔗</a> **[NASA]** NASA, Partners Clear Axiom Space’s Third Private Astronaut Crew


  - <a href="https://go4liftoff.com/launch/id/da48063e-b50f-4602-adab-ad7331ee6d82" >🚀</a> **Falcon 9 Block 5 | Axiom Space Mission 3** from Kennedy Space Center, FL, USA



- <a href="http://www.nasa.gov/press-release/nasa-receives-decadal-survey-on-biological-physical-sciences-research" >🔗</a> **[NASA]** NASA Receives Decadal Survey on Biological, Physical Sciences Research


- <a href="https://spacenews.com/neuraspace-platform-assets-jump-tenfold/" >🔗</a> **[SpaceNews]** NeuraSpace platform assets jump tenfold




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
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230913T031406">2023-09-13 03:14:06 UTC</a>
  <br>
</div>