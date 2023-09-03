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
- <a href="https://www.nasaspaceflight.com/2023/09/crew-6-splashdown/" >🔗</a> **[NASASpaceflight]** SpaceX crew to return to Earth after six-month ISS Stay


  - <a href="https://go4liftoff.com/launch/id/bc325945-4bee-4412-84e1-14998b2eba5f" >🚀</a> **Falcon 9 Block 5 | Crew-6** from Kennedy Space Center, FL, USA




  - <a href="https://go4liftoff.com/event/id/771" >📆</a> **SpaceX Crew-6 Crew Dragon Undocking**

  - <a href="https://go4liftoff.com/event/id/772" >📆</a> **SpaceX Crew-6 Crew Dragon Splashdown**


- <a href="https://www.nasaspaceflight.com/2023/09/lm-nasa-orion-artemis-iii-iv/" >🔗</a> **[NASASpaceflight]** Lockheed Martin, NASA lining up next Orion spacecraft for Artemis III and IV


  - <a href="https://go4liftoff.com/launch/id/8034d81b-af96-460c-a7b7-5c8e7f1a1d86" >🚀</a> **SLS Block 1 | Artemis III** from Kennedy Space Center, FL, USA

  - <a href="https://go4liftoff.com/launch/id/372d94b1-88fe-4cc5-9296-d893c9fa9426" >🚀</a> **SLS Block 1B | Artemis IV** from Kennedy Space Center, FL, USA



- <a href="http://www.nasa.gov/press-release/coverage-set-as-nasa-s-spacex-crew-6-prepares-for-splashdown" >🔗</a> **[NASA]** Coverage Set as NASA’s SpaceX Crew-6 Prepares for Splashdown


  - <a href="https://go4liftoff.com/launch/id/bc325945-4bee-4412-84e1-14998b2eba5f" >🚀</a> **Falcon 9 Block 5 | Crew-6** from Kennedy Space Center, FL, USA




  - <a href="https://go4liftoff.com/event/id/771" >📆</a> **SpaceX Crew-6 Crew Dragon Undocking**

  - <a href="https://go4liftoff.com/event/id/772" >📆</a> **SpaceX Crew-6 Crew Dragon Splashdown**


- <a href="https://spacenews.com/spacex-launches-13-satellites-for-u-s-space-development-agency/" >🔗</a> **[SpaceNews]** SpaceX launches 13 satellites for U.S. Space Development Agency


  - <a href="https://go4liftoff.com/launch/id/9248a1d0-393f-469a-b9c6-19470247e6fd" >🚀</a> **Falcon 9 Block 5 | SDA Tranche 0B** from Vandenberg SFB, CA, USA



- <a href="https://europeanspaceflight.com/esa-complete-full-duration-hot-fire-test-of-ariane-6-second-stage/" >🔗</a> **[European Spaceflight]** ESA Complete Full-Duration Hot Fire Test of Ariane 6 Second Stage


  - <a href="https://go4liftoff.com/launch/id/3e461ec0-8b64-4804-b9aa-e1e1f066065a" >🚀</a> **Ariane 62 | Maiden Flight** from Kourou, French Guiana



- <a href="https://tlpnetwork.com/news/2023/09/microsoft-partners-with-synthetaic-on-ai-and-data-analysis" >🔗</a> **[The Launch Pad]** Microsoft Partners With Synthetaic On AI And Data Analysis


- <a href="https://tlpnetwork.com/news/2023/09/nasa-prepares-for-osirisrex-asteroid-sample-reentry-and-landing" >🔗</a> **[The Launch Pad]** NASA Prepares For OSIRIS-REx Asteroid Sample ReEntry & Landing


  - <a href="https://go4liftoff.com/launch/id/0bcc6850-4c51-4b08-aa19-0b3753351b9b" >🚀</a> **Atlas V 411 | OSIRIS-REx** from Cape Canaveral, FL, USA




  - <a href="https://go4liftoff.com/event/id/36" >📆</a> **OSIRIS-Rex Sample Return**


- <a href="https://tlpnetwork.com/news/2023/09/nasa-confirms-new-frontiers-program-delay" >🔗</a> **[The Launch Pad]** NASA Confirms New Frontiers Program Delay


- <a href="https://www.nasaspaceflight.com/2023/09/india-aditya-l1-pslv/" >🔗</a> **[NASASpaceflight]** India launches first solar research mission, Aditya-L1, aboard PSLV


  - <a href="https://go4liftoff.com/launch/id/769470b6-7cac-41ab-9dd2-69c7e9504b1a" >🚀</a> **PSLV-XL | Aditya-L1** from Satish Dhawan Space Centre, India



- <a href="https://spacepolicyonline.com/news/nasas-lro-spots-likely-luna-25-crash-site/" >🔗</a> **[SpacePolicyOnline.com]** NASA’s LRO Spots Likely Luna-25 Crash Site


  - <a href="https://go4liftoff.com/launch/id/d8d10fbf-b900-40c7-95ef-fb2f07489f6f" >🚀</a> **Atlas V 401 | LRO/LCROSS** from Cape Canaveral, FL, USA

  - <a href="https://go4liftoff.com/launch/id/2277b184-5a07-4a71-90ce-367f41420eaa" >🚀</a> **Soyuz 2.1b/Fregat-M | Luna 25** from Vostochny Cosmodrome, Siberia, Russian Federation





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
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230903T191018">2023-09-03 19:10:18 UTC</a>
  <br>
</div>