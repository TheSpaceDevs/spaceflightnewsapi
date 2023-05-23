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
- <a href="https://spacenews.com/orbital-sidekick-acquires-first-light-imagery/" >🔗</a> **[SpaceNews]** Orbital Sidekick acquires first light imagery


  - <a href="https://go4liftoff.com/launch/id/d8bd2b25-129b-4ab7-95d9-fb8ad1fdd73e" >🚀</a> **Falcon 9 Block 5 | Transporter 7 (Dedicated SSO Rideshare)** from Vandenberg SFB, CA, USA



- <a href="https://spacenews.com/l3harris-wins-iarpa-haystac-contract/" >🔗</a> **[SpaceNews]** L3Harris wins IARPA HAYSTAC contract


- <a href="https://spacenews.com/nga-to-map-lunar-geography-to-enable-gps-on-the-moon/" >🔗</a> **[SpaceNews]** NGA to map lunar geography to enable GPS on the moon


- <a href="https://spacenews.com/nato-faces-hurdles-in-acquiring-commercial-satellite-imagery/" >🔗</a> **[SpaceNews]** NATO faces hurdles in acquiring commercial satellite imagery


- <a href="https://www.cnbc.com/2023/05/22/spacex-joining-faa-to-fight-environmental-lawsuit-over-starship.html" >🔗</a> **[CNBC]** SpaceX set to join FAA to fight environmental lawsuit that could delay Starship work


  - <a href="https://go4liftoff.com/launch/id/e32d375f-0d6e-4e54-b4f2-2b49db657fca" >🚀</a> **Starship | Integrated Flight Test** from SpaceX Space Launch Facility, TX, USA



- <a href="https://www.nasaspaceflight.com/2023/05/spacex-progressing-next-flights/" >🔗</a> **[NASASpaceflight]** SpaceX making progress toward next Starship test flights


- <a href="http://www.nasa.gov/press-release/nasa-mission-to-study-ice-clouds-help-observe-our-dynamic-atmosphere" >🔗</a> **[NASA]** NASA Mission to Study Ice Clouds, Help Observe Our Dynamic Atmosphere


- <a href="https://spacenews.com/oneweb-announces-innovation-challenge-winners/" >🔗</a> **[SpaceNews]** OneWeb announces Innovation Challenge Winners


- <a href="https://spacenews.com/exploration-upper-stage-unveiled-revolutionary-leap-in-crew-safety-cargo-capacity-and-deep-space-power/" >🔗</a> **[SpaceNews]** Exploration Upper Stage Unveiled: Revolutionary Leap in Crew Safety, Cargo Capacity, and Deep Space Power


  - <a href="https://go4liftoff.com/launch/id/372d94b1-88fe-4cc5-9296-d893c9fa9426" >🚀</a> **SLS Block 1B | Artemis IV** from Kennedy Space Center, FL, USA



- <a href="https://spacenews.com/darpa-selects-umbra-to-demonstrate-radar-imaging-techniques/" >🔗</a> **[SpaceNews]** DARPA selects Umbra to demonstrate radar imaging techniques




## Latest Blog Posts 🪧

- <a href="https://www.planetary.org/the-downlink/moon-spying-missions-and-a-planetary-evil-twin" >🔗</a> **[Planetary Society]** Moon-spying missions and a planetary evil twin


- <a href="https://blog.ulalaunch.com/blog/hypersonic-missiles-are-just-misunderstood" >🔗</a> **[United Launch Alliance]** Hypersonic Missiles are Just Misunderstood


- <a href="https://www.planetary.org/articles/why-is-venus-called-earths-twin" >🔗</a> **[Planetary Society]** Why is Venus called Earth’s twin?


- <a href="https://www.planetary.org/the-downlink/hard-working-spacecraft-and-even-harder-working-microbes" >🔗</a> **[Planetary Society]** Hard-working spacecraft and even harder-working microbes


- <a href="https://www.planetary.org/articles/why-has-spacexs-starship-sparked-an-environmental-controversy" >🔗</a> **[Planetary Society]** Why has SpaceX's Starship sparked an environmental controversy?


- <a href="https://www.planetary.org/articles/how-did-earth-get-its-oxygen" >🔗</a> **[Planetary Society]** How did Earth get its oxygen?


- <a href="https://www.planetary.org/careers/freelance-digital-advertising-specialist-contract-part-time" >🔗</a> **[Planetary Society]** Freelance Digital Advertising Specialist (Contract & Part-time)


- <a href="https://www.planetary.org/the-downlink/moonshadow-moonshadow" >🔗</a> **[Planetary Society]** Moonshadow, Moonshadow


- <a href="https://blog.ulalaunch.com/blog/why-is-stem-education-a-national-imperative" >🔗</a> **[United Launch Alliance]** Why is STEM Education a National Imperative and How Are We Wasting Our Precious Human Resource?


- <a href="https://www.planetary.org/articles/what-happened-with-psyche" >🔗</a> **[Planetary Society]** What happened with Psyche?




<hr>
  <div align="center">
  This <code>README.md</code> was last auto generated at <a href="https://www.timeanddate.com/worldclock/fixedtime.html?iso=20230523T100810">2023-05-23 10:08:10 UTC</a>
  <br>
</div>