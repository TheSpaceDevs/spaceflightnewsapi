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
- European Spaceflight Update
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
- <a href="http://www.nasa.gov/press-release/nasa-sets-coverage-for-axiom-mission-2-departure-from-space-station" >🔗</a> **[NASA]** NASA Sets Coverage for Axiom Mission 2 Departure from Space Station


- <a href="https://spacenews.com/space-development-agency-planning-to-launch-13-satellites-in-late-june/" >🔗</a> **[SpaceNews]** Space Development Agency to launch 13 satellites in late June


- <a href="https://www.nasaspaceflight.com/2023/05/arabsat-7b-launch/" >🔗</a> **[NASASpaceflight]** Falcon 9 launch with Arabsat 7B set for Friday


  - <a href="https://go4liftoff.com/launch/id/d5a80dcc-105b-445f-a8c4-394d7c7825ed" >🚀</a> **Falcon 9 Block 5 | BADR-8** from Cape Canaveral, FL, USA



- <a href="https://www.teslarati.com/rocket-labs-electron-delivers-tropics-constellation-to-orbit/" >🔗</a> **[Teslarati]** Rocket Lab’s Electron delivers TROPICS constellation to orbit


- <a href="http://www.nasa.gov/press-release/nasa-pursues-lunar-terrain-vehicle-services-for-artemis-missions" >🔗</a> **[NASA]** NASA Pursues Lunar Terrain Vehicle Services for Artemis Missions


- <a href="https://spacenews.com/darpa-seeks-ai-tools-to-automate-tracking-of-satellite-sensor-data/" >🔗</a> **[SpaceNews]** DARPA seeks AI tools to automate tracking of satellite sensor data


- <a href="https://spacenews.com/software-problem-blamed-for-ispace-lunar-lander-crash/" >🔗</a> **[SpaceNews]** Software problem blamed for ispace lunar lander crash


  - <a href="https://go4liftoff.com/launch/id/2306e0bc-e1a3-4a4a-9285-e1a94073655e" >🚀</a> **Falcon 9 Block 5 | Hakuto-R M1 & Lunar Flashlight** from Cape Canaveral, FL, USA




  - <a href="https://go4liftoff.com/event/id/730" >📆</a> **Hakuto-R M1 Lunar Landing**


- <a href="https://spacenews.com/l3harris-wins-80-million-air-force-contract-for-satcom-experiments/" >🔗</a> **[SpaceNews]** L3Harris wins $80 million Air Force contract for satcom experiments


- <a href="http://www.nasa.gov/press-release/nasa-to-provide-briefing-coverage-of-spacewalks-for-station-upgrades" >🔗</a> **[NASA]** NASA to Provide Briefing, Coverage of Spacewalks for Station Upgrades



  - <a href="https://go4liftoff.com/event/id/764" >📆</a> **US EVA-87**


- <a href="http://www.nasa.gov/press-release/new-mexico-students-to-hear-from-nasa-astronauts-aboard-space-station" >🔗</a> **[NASA]** New Mexico Students to Hear from NASA Astronauts Aboard Space Station




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/the-downlink/way-out-there" >🔗</a> **[Planetary Society]** Way out there


- <a href="https://blog.ulalaunch.com/blog/vulcan-preview-of-the-flight-readiness-firing" >🔗</a> **[United Launch Alliance]** Vulcan: Preview of the Flight Readiness Firing


- <a href="https://www.planetary.org/articles/asteroid-deflection-techniques-to-save-the-earth" >🔗</a> **[Planetary Society]** Five asteroid deflection techniques to save the Earth


- <a href="https://www.planetary.org/the-downlink/moon-spying-missions-and-a-planetary-evil-twin" >🔗</a> **[Planetary Society]** Moon-spying missions and a planetary evil twin


- <a href="https://blog.ulalaunch.com/blog/hypersonic-missiles-are-just-misunderstood" >🔗</a> **[United Launch Alliance]** Hypersonic Missiles are Just Misunderstood


- <a href="https://www.planetary.org/articles/why-is-venus-called-earths-twin" >🔗</a> **[Planetary Society]** Why is Venus called Earth’s twin?


- <a href="https://www.planetary.org/the-downlink/hard-working-spacecraft-and-even-harder-working-microbes" >🔗</a> **[Planetary Society]** Hard-working spacecraft and even harder-working microbes


- <a href="https://www.planetary.org/articles/why-has-spacexs-starship-sparked-an-environmental-controversy" >🔗</a> **[Planetary Society]** Why has SpaceX's Starship sparked an environmental controversy?


- <a href="https://www.planetary.org/articles/how-did-earth-get-its-oxygen" >🔗</a> **[Planetary Society]** How did Earth get its oxygen?


- <a href="https://www.planetary.org/careers/freelance-digital-advertising-specialist-contract-part-time" >🔗</a> **[Planetary Society]** Freelance Digital Advertising Specialist (Contract & Part-time)




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230527T041614">2023-05-27 04:16:14 UTC</a>
  <br>
</div>