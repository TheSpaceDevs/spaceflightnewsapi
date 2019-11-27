[![Build Status](https://travis-ci.org/spaceflightnewsapi/spaceflightnewsapi.svg?branch=master)](https://travis-ci.org/spaceflightnewsapi/spaceflightnewsapi)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5ad094cb6a3847b48985345309d579b0)](https://www.codacy.com/app/derkweijers/spaceflightnewsapi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=spaceflightnewsapi/spaceflightnewsapi&amp;utm_campaign=Badge_Grade)
![Discord](https://img.shields.io/discord/482110141131522058.svg)
![Uptime Robot ratio (30 days)](https://img.shields.io/uptimerobot/ratio/m781471335-50a622775755ea51d2e440e5.svg)

# Spacelaunch News API
Spacelaunch News API was created as a solution for my problem when I wanted to develop an app for Spaceflight News: many (great!) news sites with different API's.

To make it easier for myself, I began a project that would aggegrate metadata from those news sites and publish them through an API. Since there are others that might benefit from this API, I decided make the API publicly available.

There are great apps out on the internet, that are connected to services like <https://www.launchlibrary.net/>. By making this API available to everyone, I hope to open new doors for the developers of these apps.

## Docs
Docs can be found at https://spaceflightnewsapi.net/api/v1/

## Currently imported news sites

* https://www.nasaspaceflight.com/
* https://www.spaceflightnow.com/
* https://www.spacex.com/
* https://www.spacenews.com/
* https://www.nasa.gov/
* https://www.esa.int/
* https://www.arstechnica.com/

## Currently imported blog sites

* http://www.planetary.org/
* https://www.jpl.nasa.gov/blog/

## Space Launch Now integration
Starting from version 1.2, we now have Space Launch Now integration. All documents have new key values
'launches' and 'events'. These are arrays that will be filled with id's from the SLN API to get the associated
launch or event. Nice if you want to combine the two in your app!

## Changelog
### v1.6.2 (27-11-2019)
* Removed the offset parameter since the page parameter offers the same functionality;
* Updated all libraries;

### v.1.5.0 (28-08-2019)
* Added the publised_date property, which is a full representation of date and time (https://jira.go4liftoff.com/browse/SNAPI-24)

### v1.4.0 (14-08-2019)
* Added a new property: featured. You can now add featured news to your applications, that has been selected by the SNAPI crew.

### v1.3.0 (01-07-2019)
* Added Launch Library integration

### v1.2.0 (11-06-2019)
* Added support for Space Launch Now launches and events;
* Changed to a different CMS provider;

### v1.1.1 (05-06-2019)
* Packages updated
* Fix in the documentation

### v1.1.0 (18-04-2019)
* Improved reconnect logic for MongoDB
* Re-introduced reports endpoint

### v1.0.0 (23-03-2019)
* Searching for articles is now on the /articles resource itself;
* Documentation generated from the code;
* Authentication support;
* Added support to post and delete documents;
* Metadata on the /articles and /blogs resources;
* removed since_added and since_published;
* Removed the /astronauts, /mannedflights and /iss resources. The Space Launch Now API will provide these.
* Removed the /article and /blog resource;

### v0.8.2 beta (02-12-2018)
* Since_added and since_published work again.

### v0.8.1 beta (29-11-2018)
* Getting a single article with specific articles won't result in an error anymore.

### v0.8.0 beta (28-11-2018)
* entered queries are now case-insensitive;
* added the /articles/search endpoint so you can search for articles.

### v0.7.0 beta (11-11-2018)
* /astronauts endpoint can now receive queries;
* Link to astronaut portrait added;
* Daily ISS reports are now being imported;
* /iss endpoint will have the latest daily ISS report.

### v0.6.0 beta (30-10-2018)
* Blogs endpoint added
* ISS endpoint added
* Ability to retrieve ISS expedition data
* Automated tests will now check if version was bumped

### v0.5.0 beta (27-09-2018)
* Added pagination
* Added /info endpoint
* Added version info to /info endpoint
* Added total article count to /info endpoint
* Heroku upgraded from stack 16 to 18

### v0.4.0 beta (17-09-2018)
* Now possible to search on the same key multiple times

### v0.3.0 beta (12-09-2018)
* 'id' tag removed from the response
* Added 'news_site_long' to the model

### v0.2.0 beta (03-09-2018)
* Better logging
* Automated testing
* Get articles since n time

### v0.1.0 beta (03-09-2018)
* Get a list of the latest articles
* Find articles on title, category and tag
* Find articles on only category or tag
* Find all articles by a news site
* Find article by its ID
