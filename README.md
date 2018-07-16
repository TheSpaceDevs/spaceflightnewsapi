# Spacelaunch News API
Spacelaunch News API was created as a solution for my problem when I wanted to develop an app for Spaceflight News: many (great!) news sites with different API's. 

To make it easier for myself, I began a project that would aggegrate metadata from those news sites and publish them through an API. Since there are others that might benefit from this API, I decided make the API publicly available.

There are great apps out on the internet, that are connected to services like https://www.launchlibrary.net/. By making this API available to everyone, I hope to open new doors for the developers of these apps.

## Acknowledgments
I'd like thank/mention the following people/groups/services:

* `Jared Petersen - (https://github.com/jaredpetersen/nodejs-api-template)`: Used template for this API;

## Endpoints
* `GET /articles/newssite/:newssite`: List all articles by a particular news site;
* `GET /articles/category/:category`: List all articles from a specific catagory;
* `GET /articles/tag/:tag`: List all articles from a specific tag;

## Currently imported news sites

* https://www.nasaspaceflight.com/