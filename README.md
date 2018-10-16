# Spacelaunch News API
Spacelaunch News API was created as a solution for my problem when I wanted to develop an app for Spaceflight News: many (great!) news sites with different API's.

To make it easier for myself, I began a project that would aggegrate metadata from those news sites and publish them through an API. Since there are others that might benefit from this API, I decided make the API publicly available.

There are great apps out on the internet, that are connected to services like https://www.launchlibrary.net/. By making this API available to everyone, I hope to open new doors for the developers of these apps.

## Acknowledgments
I'd like thank/mention the following people/groups/services:

* `Jared Petersen - (https://github.com/jaredpetersen/nodejs-api-template)`: Used template for this API;

## Currently imported news sites

* https://www.nasaspaceflight.com/
* https://www.spaceflightnow.com/
* https://www.spacex.com/
* https://www.space.com/

## Changelog
### v0.6.0 beta (TBD)
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
