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
- <a href="https://spacenews.com/falcon-heavy-sends-jupiter-3-broadband-giant-toward-geostationary-orbit/" >🔗</a> **[SpaceNews]** Falcon Heavy sends Jupiter-3 broadband giant toward geostationary orbit


  - <a href="https://go4liftoff.com/launch/id/72491a20-315d-4aea-b6df-d1202930bd60" >🚀</a> **Falcon Heavy | EchoStar 24/Jupiter-3** from Kennedy Space Center, FL, USA



- <a href="https://tlpnetwork.com/news/2023/07/esa-deorbits-aeolus-spacecraft" >🔗</a> **[The Launch Pad]** DEVELOPING STORY: ESA DeOrbits Aeolus Spacecraft, Concluding 5 Year Mission


  - <a href="https://go4liftoff.com/launch/id/68ab2654-f5ed-431f-a2cc-dbb392b4d7d8" >🚀</a> **Vega | ADM-Aeolus** from Kourou, French Guiana



- <a href="https://spacenews.com/sierra-space-wins-air-force-contract-for-upper-stage-engine-development/" >🔗</a> **[SpaceNews]** Sierra Space wins Air Force contract for upper-stage engine development


- <a href="https://tlpnetwork.com/news/2023/07/l3harris-acquires-aerojet-rocketdyne" >🔗</a> **[The Launch Pad]** L3Harris Acquires Aerojet Rocketdyne


- <a href="https://tlpnetwork.com/news/2023/07/argentina-signs-artemis-accords" >🔗</a> **[The Launch Pad]** Argentina 28th Country To Sign Artemis Accords


- <a href="http://www.nasa.gov/press-release/nasa-awards-administrative-technical-support-services-contract" >🔗</a> **[NASA]** NASA Awards Administrative & Technical Support Services Contract


- <a href="https://spacenews.com/ula-has-concerns-about-a-third-competitor-in-national-security-space-launch/" >🔗</a> **[SpaceNews]** ULA has concerns about a third competitor in national security space launch


- <a href="https://spacenews.com/aerojet-rocketdyne-officially-becomes-part-of-l3harris/" >🔗</a> **[SpaceNews]** Aerojet Rocketdyne officially becomes part of L3Harris


- <a href="https://tlpnetwork.com/news/2023/07/starship-ift-1-launch-wb57-footage-released" >🔗</a> **[The Launch Pad]** STARSHIP IFT-1 Launch WB-57 Footage Released


  - <a href="https://go4liftoff.com/launch/id/e32d375f-0d6e-4e54-b4f2-2b49db657fca" >🚀</a> **Starship | Integrated Flight Test** from SpaceX Space Launch Facility, TX, USA



- <a href="https://arstechnica.com/space/2023/07/nasa-temporarily-loses-contact-with-one-of-its-most-distant-spacecraft/" >🔗</a> **[Arstechnica]** NASA temporarily loses contact with one of its most distant spacecraft


  - <a href="https://go4liftoff.com/launch/id/75414835-ec0a-43f4-b624-1636502312f3" >🚀</a> **Titan IIIE | Voyager 2** from Cape Canaveral, FL, USA





## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/the-downlink/aquatic-equivalencies" >🔗</a> **[Planetary Society]** Aquatic equivalencies


- <a href="https://www.planetary.org/articles/life-on-venus-your-questions-answered" >🔗</a> **[Planetary Society]** Life on Venus: Your Questions Answered


- <a href="https://europeanspaceflight.substack.com/p/the-time-europe-tried-to-copy-energia" >🔗</a> **[European Spaceflight]** The time Europe tried to copy Energia


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-july-17-23-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: July 17-23, 2023


- <a href="https://europeanspaceflight.substack.com/p/how-can-thales-use-space-rider-ip" >🔗</a> **[European Spaceflight]** How can Thales use Space Rider IP for Rev-1?


- <a href="https://www.planetary.org/the-downlink/thats-a-mare" >🔗</a> **[Planetary Society]** That’s a mare


- <a href="https://www.planetary.org/articles/the-senate-threatens-to-cancel-mars-sample-return" >🔗</a> **[Planetary Society]** The U.S. Senate threatens to cancel Mars Sample Return


- <a href="https://spacepolicyonline.com/news/weekly-roundup-for-spacepolicyonline-com-july-3-16-2023/" >🔗</a> **[SpacePolicyOnline.com]** Weekly Roundup for SpacePolicyOnline.com: July 3-16, 2023


- <a href="https://europeanspaceflight.substack.com/p/a-little-boost-goes-a-long-way" >🔗</a> **[European Spaceflight]** A little Boost! goes a long way


- <a href="https://www.planetary.org/the-downlink/speedy-spacecraft-and-pretty-pics" >🔗</a> **[Planetary Society]** Speedy spacecraft and pretty pics




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230729T191012">2023-07-29 19:10:12 UTC</a>
  <br>
</div>