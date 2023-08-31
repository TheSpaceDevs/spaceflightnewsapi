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
- <a href="https://www.teslarati.com/spacex-9th-launch-august-2023/" >🔗</a> **[Teslarati]** SpaceX set for 9th launch of the month


- <a href="https://www.teslarati.com/firefly-aerospace-victus-nox-mission/" >🔗</a> **[Teslarati]** Firefly Aerospace announces they are ready for the Victus Nox mission


- <a href="https://www.cnbc.com/2023/08/31/investing-in-space-why-the-pentagon-is-spending-billions-on-a-satellite-constellation.html" >🔗</a> **[CNBC]** Investing in Space: Why the Pentagon is spending billions to build its own satellite constellation


- <a href="https://www.nasaspaceflight.com/2023/08/ship-25-awaits-rollout-for-full-stack-of-starship-flight-2/" >🔗</a> **[NASASpaceflight]** Ship 25 awaits rollout for full-stack of Starship Flight 2


- <a href="https://tlpnetwork.com/news/2023/08/space-engine-systems-tour-and-interview-with-pradeep-dass" >🔗</a> **[The Launch Pad]** The Future Of Hypersonic Flight | TLP Exclusive Tour & Interview


- <a href="https://spacenews.com/qinetiq-wins-224-million-contract-to-provide-technical-services-to-space-development-agency/" >🔗</a> **[SpaceNews]** QinetiQ wins $224 million contract to provide technical services to Space Development Agency


- <a href="https://europeanspaceflight.com/eu-member-states-commit-to-not-test-direct-ascent-asat-systems/" >🔗</a> **[European Spaceflight]** EU Member States Commit to Not Test Direct-Ascent ASAT Systems


- <a href="https://spacenews.com/satixfy-sells-satellite-payload-subsidiary-to-mda/" >🔗</a> **[SpaceNews]** SatixFy sells satellite payload subsidiary to MDA


- <a href="https://www.nasaspaceflight.com/2023/08/tranche-0-flight-2/" >🔗</a> **[NASASpaceflight]** SpaceX scrubs second launch for Space Development Agency’s Tranche 0, but still on for Starlink mission


  - <a href="https://go4liftoff.com/launch/id/9248a1d0-393f-469a-b9c6-19470247e6fd" >🚀</a> **Falcon 9 Block 5 | SDA Tranche 0B** from Vandenberg SFB, CA, USA



- <a href="https://spacenews.com/nasa-gears-up-for-return-of-osiris-rex-asteroid-sample/" >🔗</a> **[SpaceNews]** NASA gears up for return of OSIRIS-REx asteroid sample


  - <a href="https://go4liftoff.com/launch/id/0bcc6850-4c51-4b08-aa19-0b3753351b9b" >🚀</a> **Atlas V 411 | OSIRIS-REx** from Cape Canaveral, FL, USA




  - <a href="https://go4liftoff.com/event/id/36" >📆</a> **OSIRIS-Rex Sample Return**




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/space-missions/change-6-collecting-the-first-lunar-farside-samples" >🔗</a> **[Planetary Society]** Chang'e-6, collecting the first lunar farside samples


- <a href="https://europeanspaceflight.substack.com/p/does-european-sci-comm-suck" >🔗</a> **[European Spaceflight]** Does European Sci-Comm Suck?


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-august-21-27-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: August 21-27, 2023


- <a href="https://blog.ulalaunch.com/blog/rocketstars-a-life-that-spans-the-atlas-v-program" >🔗</a> **[United Launch Alliance]** RocketStars: A life that spans the Atlas V program


- <a href="https://www.planetary.org/the-downlink/moonstruck" >🔗</a> **[Planetary Society]** Moonstruck


- <a href="https://blog.ulalaunch.com/blog/rocketstars-engineer-moves-from-aircraft-to-launching-satellites-at-ula" >🔗</a> **[United Launch Alliance]** RocketStars: Engineer moves from aircraft to launching satellites at ULA


- <a href="https://www.planetary.org/articles/what-would-happen-if-an-asteroid-hit-the-moon" >🔗</a> **[Planetary Society]** What would happen if an asteroid hit the Moon?


- <a href="https://blog.ulalaunch.com/blog/silentbarker/nrol-107-payload-mate-mounted-to-atlas-v-for-launch" >🔗</a> **[United Launch Alliance]** SILENTBARKER/NROL-107: Payload mounted to Atlas V for launch


- <a href="https://www.planetary.org/articles/total-solar-eclipse-2024-path-of-totality" >🔗</a> **[Planetary Society]** Total solar eclipse 2024: Why it’s worth getting into the path of totality


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-august-14-20-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: August 14-20, 2023




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230831T201428">2023-08-31 20:14:28 UTC</a>
  <br>
</div>