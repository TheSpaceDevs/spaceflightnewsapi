/**
 * @api {get} /v1/articles Get articles
 * @apiName GetArticles
 * @apiGroup Articles
 * @apiVersion 1.0.0
 * @apiDescription Retrieves a list of articles. You can query this endpoint with parameter 'news_site' to return
 * articles provided by a particular news site. This endpoint can also be queried with 'search' to search
 * for articles which match your search parameter.
 *
 * Also supports page, limit, offset and sort options.
 *
 * @apiExample Search for articles
 * https://spaceflightnewsapi.net/api/v1/articles?search=dragon
 *
 * @apiExample Search for articles published by SpaceX
 * https://spaceflightnewsapi.net/api/v1/articles?news_site=spacex
 *
 * @apiParam {String} title Title of the article.
 * @apiParam {String} news_site News site that published the article.
 * @apiParam {String} news_site_long Unformatted name of the news site that published the article.
 * @apiParam {String} url URL of the article.
 * @apiParam {String} featured_image Featured image of the article.
 * @apiParam {Number} id ID from the news site.
 * @apiParam {String} _id ID generated by SNAPI.
 * @apiParam {Number} date_published Date when news site added the article
 * @apiParam {Number} date_added Date when article was added to SNAPI
 * @apiParam {Array} categories Array with categories.
 * @apiParam {Array} tags Array with tags.
 *
 * @apiSuccess {String} title Title of the article.
 * @apiSuccess {String} news_site News site that published the article.
 * @apiSuccess {String} news_site_long Unformatted name of the news site that published the article.
 * @apiSuccess {String} url URL of the article.
 * @apiSuccess {String} featured_image Featured image of the article.
 * @apiSuccess {Number} id ID from the news site.
 * @apiSuccess {String} _id ID generated by SNAPI.
 * @apiSuccess {Number} date_published Date when news site added the article.
 * @apiSuccess {Number} date_added Date when article was added to SNAPI.
 * @apiSuccess {Array} categories Array with categories.
 * @apiSuccess {Array} tags Array with tags.
 *
 * @apiSuccessExample Success-Response:
 * HTTP/1.1 200 OK
 * {
 *   "docs": [
 *     {
 *
 *     }
 *   ],
 *   "totalDocs": 719,
 *   "limit": 10,
 *   "hasPrevPage": false,
 *   "hasNextPage": true,
 *   "page": 1,
 *   "totalPages": 72,
 *   "prevPage": null,
 *   "nextPage": 2
 * }
 *
 *
 * @apiErrorExample Error-Response:
 *     HTTP/1.1 400 Bad request
 *     {
 *       "message": "Uh-oh, something went wrong. Please try again!"
 *     }
 */

/**
 * @api {get} /v1/blogs Get blogs
 * @apiName GetBlogs
 * @apiGroup Blogs
 * @apiVersion 1.0.0
 * @apiDescription Retrieves a list of blogs. You can query this endpoint with parameter 'news_site' to return
 * blogs provided by a particular news site. This endpoint can also be queried with 'search' to search
 * for blogs which match your search parameter.
 *
 * Also supports page, limit, offset and sort options.
 *
 * @apiExample Search for blogs
 * https://spaceflightnewsapi.net/api/v1/blogs?search=bennu
 *
 * @apiExample Search for articles published by SpaceX
 * https://spaceflightnewsapi.net/api/v1/blogs?news_site=planetarysociety
 *
 * @apiParam {String} title Title of the blog.
 * @apiParam {String} news_site News site that published the blog.
 * @apiParam {String} news_site_long Unformatted name of the news site that published the blog.
 * @apiParam {String} url URL of the blog.
 * @apiParam {String} featured_image Featured image of the blog.
 * @apiParam {Number} id ID from the news site.
 * @apiParam {String} _id ID generated by SNAPI.
 * @apiParam {Number} date_published Date when news site added the blog
 * @apiParam {Number} date_added Date when blog was added to SNAPI
 * @apiParam {Array} categories Array with categories.
 * @apiParam {Array} tags Array with tags.
 *
 * @apiSuccess {String} title Title of the blogs.
 * @apiSuccess {String} news_site News site that published the blog.
 * @apiSuccess {String} news_site_long Unformatted name of the news site that published the blog.
 * @apiSuccess {String} url URL of the blog.
 * @apiSuccess {String} featured_image Featured image of the blog.
 * @apiSuccess {Number} id ID from the news site.
 * @apiSuccess {String} _id ID generated by SNAPI.
 * @apiSuccess {Number} date_published Date when news site added the blog.
 * @apiSuccess {Number} date_added Date when blog was added to SNAPI.
 * @apiSuccess {Array} categories Array with categories.
 * @apiSuccess {Array} tags Array with tags.
 *
 * @apiSuccessExample Success-Response:
 * HTTP/1.1 200 OK
 * {
 *   "docs": [
 *     {
 *
 *     }
 *   ],
 *   "totalDocs": 719,
 *   "limit": 10,
 *   "hasPrevPage": false,
 *   "hasNextPage": true,
 *   "page": 1,
 *   "totalPages": 72,
 *   "prevPage": null,
 *   "nextPage": 2
 * }
 *
 *
 * @apiErrorExample Error-Response:
 *     HTTP/1.1 400 Bad request
 *     {
 *       "message": "Uh-oh, something went wrong. Please try again!"
 *     }
 */

/**
 * @api {get} /api/v1/articles Get articles
 * @apiName GetArticles
 * @apiGroup Articles
 * @apiVersion 1.2.0
 * @apiDescription Retrieves a list of articles. You can query this endpoint with parameter 'news_site' to return
 * articles provided by a particular news site. This endpoint can also be queried with 'search' to search
 * for articles which match your search parameter.
 *
 * Also supports page, limit, offset and sort options.
 *
 * @apiExample Search for articles
 * https://spaceflightnewsapi.net/api/v1/articles?search=dragon
 *
 * @apiExample Search for articles published by SpaceX
 * https://spaceflightnewsapi.net/api/v1/articles?news_site=spacex
 *
 * @apiExample Search for a SLN API launch ID
 * https://spaceflightnewsapi.net/api/v1/articles?launches=b347b02e-18b4-4e55-ac9e-6bebecbc6858
 *
 * @apiParam {String} title Title of the article.
 * @apiParam {String} news_site News site that published the article.
 * @apiParam {String} news_site_long Unformatted name of the news site that published the article.
 * @apiParam {String} url URL of the article.
 * @apiParam {String} featured_image Featured image of the article.
 * @apiParam {Number} id ID from the news site.
 * @apiParam {String} _id ID generated by SNAPI.
 * @apiParam {Number} date_published Date when news site added the article
 * @apiParam {Number} date_added Date when article was added to SNAPI
 * @apiParam {String} launches ID that maps to a launch in the SLN API
 * @apiParam {String} events ID that maps to an event in the SLN API
 * @apiParam {String} ll ID that maps to a launch from the Launch Library
 *
 * @apiSuccess {String} title Title of the article.
 * @apiSuccess {String} news_site News site that published the article.
 * @apiSuccess {String} news_site_long Unformatted name of the news site that published the article.
 * @apiSuccess {String} url URL of the article.
 * @apiSuccess {String} featured_image Featured image of the article.
 * @apiSuccess {Number} id ID from the news site.
 * @apiSuccess {String} _id ID generated by SNAPI.
 * @apiSuccess {Number} date_published Date when news site added the article.
 * @apiSuccess {Number} date_added Date when article was added to SNAPI.
 * @apiSuccess {Array} categories Array with categories.
 * @apiSuccess {Array} tags Array with tags.
 * @apiSuccess {Array} launches Array with SLN API launch ID's.
 * @apiSuccess {Array} events Array with SLN API event ID's.
 * @apiSuccess {Array} ll Array with Launch Library launch ID's.
 *
 * @apiSuccessExample Success-Response:
 * HTTP/1.1 200 OK
 * {
 *   "docs": [
 *     {
 *
 *     }
 *   ],
 *   "totalDocs": 719,
 *   "limit": 10,
 *   "hasPrevPage": false,
 *   "hasNextPage": true,
 *   "page": 1,
 *   "totalPages": 72,
 *   "prevPage": null,
 *   "nextPage": 2
 * }
 *
 *
 * @apiErrorExample Error-Response:
 *     HTTP/1.1 400 Bad request
 *     {
 *       "message": "Uh-oh, something went wrong. Please try again!"
 *     }
 */


/**
 * @api {get} /api/v1/blogs Get blogs
 * @apiName GetBlogs
 * @apiGroup Blogs
 * @apiVersion 1.2.0
 * @apiDescription Retrieves a list of blogs. You can query this endpoint with parameter 'news_site' to return
 * blogs provided by a particular news site. This endpoint can also be queried with 'search' to search
 * for blogs which match your search parameter.
 *
 * Also supports page, limit, offset and sort options.
 *
 * @apiExample Search for blogs
 * https://spaceflightnewsapi.net/api/v1/blogs?search=bennu
 *
 * @apiExample Search for articles published by SpaceX
 * https://spaceflightnewsapi.net/api/v1/blogs?news_site=planetarysociety
 *
 * @apiExample Search for a SLN API launch ID
 * https://spaceflightnewsapi.net/api/v1/blogs?launches=b347b02e-18b4-4e55-ac9e-6bebecbc6858
 *
 * @apiParam {String} title Title of the blog.
 * @apiParam {String} news_site News site that published the blog.
 * @apiParam {String} news_site_long Unformatted name of the news site that published the blog.
 * @apiParam {String} url URL of the blog.
 * @apiParam {String} featured_image Featured image of the blog.
 * @apiParam {Number} id ID from the news site.
 * @apiParam {String} _id ID generated by SNAPI.
 * @apiParam {Number} date_published Date when news site added the blog
 * @apiParam {Number} date_added Date when blog was added to SNAPI
 * @apiParam {String} launches ID that maps to a launch in the SLN API
 * @apiParam {String} events ID that maps to an event in the SLN API
 *
 * @apiSuccess {String} title Title of the blogs.
 * @apiSuccess {String} news_site News site that published the blog.
 * @apiSuccess {String} news_site_long Unformatted name of the news site that published the blog.
 * @apiSuccess {String} url URL of the blog.
 * @apiSuccess {String} featured_image Featured image of the blog.
 * @apiSuccess {Number} id ID from the news site.
 * @apiSuccess {String} _id ID generated by SNAPI.
 * @apiSuccess {Number} date_published Date when news site added the blog.
 * @apiSuccess {Number} date_added Date when blog was added to SNAPI.
 * @apiSuccess {Array} categories Array with categories.
 * @apiSuccess {Array} tags Array with tags.
 * @apiSuccess {Array} launches Array with SLN API launch ID's.
 * @apiSuccess {Array} events Array with SLN API event ID's.
 *
 * @apiSuccessExample Success-Response:
 * HTTP/1.1 200 OK
 * {
 *   "docs": [
 *     {
 *
 *     }
 *   ],
 *   "totalDocs": 719,
 *   "limit": 10,
 *   "hasPrevPage": false,
 *   "hasNextPage": true,
 *   "page": 1,
 *   "totalPages": 72,
 *   "prevPage": null,
 *   "nextPage": 2
 * }
 *
 *
 * @apiErrorExample Error-Response:
 *     HTTP/1.1 400 Bad request
 *     {
 *       "message": "Uh-oh, something went wrong. Please try again!"
 *     }
 */

/**
 * @api {get} /api/v1/reports Get reports
 * @apiName GetReports
 * @apiGroup Reports
 * @apiVersion 1.1.0
 * @apiDescription Retrieves a list of reports. You can query this endpoint with parameter 'news_site' to return
 * reports provided by a particular news site. This endpoint can also be queried with 'search' to search
 * for reports which match your search parameter.
 *
 * Also supports page, limit, offset and sort options.
 *
 * @apiExample Search for reports
 * https://spaceflightnewsapi.net/api/v1/reports?search=iss
 *
 * @apiExample Search for reports published by NASA
 * https://spaceflightnewsapi.net/api/v1/reports?news_site=nasa
 *
 * @apiParam {String} title Title of the report.
 * @apiParam {String} news_site News site that published the report.
 * @apiParam {String} news_site_long Unformatted name of the news site that published the report.
 * @apiParam {String} url URL of the report.
 * @apiParam {Number} _id ID generated by SNAPI.
 * @apiParam {Number} date_published Date when news site added the report
 * @apiParam {Number} date_added Date when report was added to SNAPI
 *
 * @apiSuccess {String} title Title of the report.
 * @apiSuccess {String} news_site News site that published the report.
 * @apiSuccess {String} news_site_long Unformatted name of the news site that published the report.
 * @apiSuccess {String} url URL of the report.
 * @apiSuccess {Number} _id ID generated by SNAPI.
 * @apiSuccess {Number} date_published Date when news site added the report.
 * @apiSuccess {Number} date_added Date when report was added to SNAPI.
 *
 * @apiSuccessExample Success-Response:
 * HTTP/1.1 200 OK
 * {
 *   "docs": [
 *     {
 *
 *     }
 *   ],
 *   "totalDocs": 719,
 *   "limit": 10,
 *   "hasPrevPage": false,
 *   "hasNextPage": true,
 *   "page": 1,
 *   "totalPages": 72,
 *   "prevPage": null,
 *   "nextPage": 2
 * }
 *
 *
 * @apiErrorExample Error-Response:
 *     HTTP/1.1 400 Bad request
 *     {
 *       "message": "Uh-oh, something went wrong. Please try again!"
 *     }
 */

/**
 * @api {get} /api/v1/articles Get articles
 * @apiName GetArticles
 * @apiGroup Articles
 * @apiVersion 1.5.1
 * @apiDescription Retrieves a list of articles. You can query this endpoint with parameter 'news_site' to return
 * articles provided by a particular news site. This endpoint can also be queried with 'search' to search
 * for articles which match your search parameter.
 *
 * Also supports page, limit, offset and sort options.
 *
 * @apiExample Search for articles
 * https://spaceflightnewsapi.net/api/v1/articles?search=dragon
 *
 * @apiExample Search for articles published by SpaceX
 * https://spaceflightnewsapi.net/api/v1/articles?news_site=spacex
 *
 * @apiExample Search for a SLN API launch ID
 * https://spaceflightnewsapi.net/api/v1/articles?launches=b347b02e-18b4-4e55-ac9e-6bebecbc6858
 *
 * @apiParam {String} title Title of the article.
 * @apiParam {String} news_site News site that published the article.
 * @apiParam {String} news_site_long Unformatted name of the news site that published the article.
 * @apiParam {String} url URL of the article.
 * @apiParam {String} featured_image Featured image of the article.
 * @apiParam {Number} id ID from the news site.
 * @apiParam {String} _id ID generated by SNAPI.
 * @apiParam {Number} date_published Date when news site added the article
 * @apiParam {Number} date_added Date when article was added to SNAPI
 * @apiParam {Date} published_date Date when news site added the article (full-time representation)
 * @apiParam {Date} imported_date Date when the article was added to SNAPI (full-time representation)
 * @apiParam {String} launches ID that maps to a launch in the SLN API
 * @apiParam {String} events ID that maps to an event in the SLN API
 * @apiParam {String} ll ID that maps to a launch from the Launch Library
 *
 * @apiSuccess {String} title Title of the article.
 * @apiSuccess {String} news_site News site that published the article.
 * @apiSuccess {String} news_site_long Unformatted name of the news site that published the article.
 * @apiSuccess {String} url URL of the article.
 * @apiSuccess {String} featured_image Featured image of the article.
 * @apiSuccess {Number} id ID from the news site.
 * @apiSuccess {String} _id ID generated by SNAPI.
 * @apiSuccess {Number} date_published Date when news site added the article.
 * @apiSuccess {Number} date_added Date when article was added to SNAPI.
 * @apiParam {Date} published_date Date when news site added the article (full-time representation)
 * @apiParam {Date} imported_date Date when the article was added to SNAPI (full-time representation)
 * @apiSuccess {Array} categories Array with categories.
 * @apiSuccess {Array} tags Array with tags.
 * @apiSuccess {Array} launches Array with SLN API launch ID's.
 * @apiSuccess {Array} events Array with SLN API event ID's.
 * @apiSuccess {Array} ll Array with Launch Library launch ID's.
 *
 * @apiSuccessExample Success-Response:
 * HTTP/1.1 200 OK
 * {
 *   "docs": [
 *     {
 *
 *     }
 *   ],
 *   "totalDocs": 719,
 *   "limit": 10,
 *   "hasPrevPage": false,
 *   "hasNextPage": true,
 *   "page": 1,
 *   "totalPages": 72,
 *   "prevPage": null,
 *   "nextPage": 2
 * }
 *
 *
 * @apiErrorExample Error-Response:
 *     HTTP/1.1 400 Bad request
 *     {
 *       "message": "Uh-oh, something went wrong. Please try again!"
 *     }
 */

/**
 * @api {get} /api/v1/blogs Get blogs
 * @apiName GetBlogs
 * @apiGroup Blogs
 * @apiVersion 1.5.1
 * @apiDescription Retrieves a list of blogs. You can query this endpoint with parameter 'news_site' to return
 * blogs provided by a particular news site. This endpoint can also be queried with 'search' to search
 * for blogs which match your search parameter.
 *
 * Also supports page, limit, offset and sort options.
 *
 * @apiExample Search for blogs
 * https://spaceflightnewsapi.net/api/v1/blogs?search=bennu
 *
 * @apiExample Search for articles published by SpaceX
 * https://spaceflightnewsapi.net/api/v1/blogs?news_site=planetarysociety
 *
 * @apiExample Search for a SLN API launch ID
 * https://spaceflightnewsapi.net/api/v1/blogs?launches=b347b02e-18b4-4e55-ac9e-6bebecbc6858
 *
 * @apiParam {String} title Title of the blog.
 * @apiParam {String} news_site News site that published the blog.
 * @apiParam {String} news_site_long Unformatted name of the news site that published the blog.
 * @apiParam {String} url URL of the blog.
 * @apiParam {String} featured_image Featured image of the blog.
 * @apiParam {Number} id ID from the news site.
 * @apiParam {String} _id ID generated by SNAPI.
 * @apiParam {Number} date_published Date when news site added the blog
 * @apiParam {Number} date_added Date when blog was added to SNAPI
 * @apiParam {Date} published_date Date when news site added the blog (full-time representation)
 * @apiParam {Date} imported_date Date when the blog was added to SNAPI (full-time representation)
 * @apiParam {String} launches ID that maps to a launch in the SLN API
 * @apiParam {String} events ID that maps to an event in the SLN API
 *
 * @apiSuccess {String} title Title of the blogs.
 * @apiSuccess {String} news_site News site that published the blog.
 * @apiSuccess {String} news_site_long Unformatted name of the news site that published the blog.
 * @apiSuccess {String} url URL of the blog.
 * @apiSuccess {String} featured_image Featured image of the blog.
 * @apiSuccess {Number} id ID from the news site.
 * @apiSuccess {String} _id ID generated by SNAPI.
 * @apiSuccess {Number} date_published Date when news site added the blog.
 * @apiSuccess {Number} date_added Date when blog was added to SNAPI.
 * @apiParam {Date} published_date Date when news site added the blog (full-time representation)
 * @apiParam {Date} imported_date Date when the blog was added to SNAPI (full-time representation)
 * @apiSuccess {Array} categories Array with categories.
 * @apiSuccess {Array} tags Array with tags.
 * @apiSuccess {Array} launches Array with SLN API launch ID's.
 * @apiSuccess {Array} events Array with SLN API event ID's.
 *
 * @apiSuccessExample Success-Response:
 * HTTP/1.1 200 OK
 * {
 *   "docs": [
 *     {
 *
 *     }
 *   ],
 *   "totalDocs": 719,
 *   "limit": 10,
 *   "hasPrevPage": false,
 *   "hasNextPage": true,
 *   "page": 1,
 *   "totalPages": 72,
 *   "prevPage": null,
 *   "nextPage": 2
 * }
 *
 *
 * @apiErrorExample Error-Response:
 *     HTTP/1.1 400 Bad request
 *     {
 *       "message": "Uh-oh, something went wrong. Please try again!"
 *     }
 */

/**
 * @api {get} /api/v1/reports Get reports
 * @apiName GetReports
 * @apiGroup Reports
 * @apiVersion 1.5.1
 * @apiDescription Retrieves a list of reports. You can query this endpoint with parameter 'news_site' to return
 * reports provided by a particular news site. This endpoint can also be queried with 'search' to search
 * for reports which match your search parameter.
 *
 * Also supports page, limit, offset and sort options.
 *
 * @apiExample Search for reports
 * https://spaceflightnewsapi.net/api/v1/reports?search=iss
 *
 * @apiExample Search for reports published by NASA
 * https://spaceflightnewsapi.net/api/v1/reports?news_site=nasa
 *
 * @apiParam {String} title Title of the report.
 * @apiParam {String} news_site News site that published the report.
 * @apiParam {String} news_site_long Unformatted name of the news site that published the report.
 * @apiParam {String} url URL of the report.
 * @apiParam {Number} _id ID generated by SNAPI.
 * @apiParam {Number} date_published Date when news site added the report
 * @apiParam {Number} date_added Date when report was added to SNAPI
 * @apiParam {Date} published_date Date when news site added the report (full-time representation)
 * @apiParam {Date} imported_date Date when report was added to SNAPI (full-time representation)
 *
 * @apiSuccess {String} title Title of the report.
 * @apiSuccess {String} news_site News site that published the report.
 * @apiSuccess {String} news_site_long Unformatted name of the news site that published the report.
 * @apiSuccess {String} url URL of the report.
 * @apiSuccess {Number} _id ID generated by SNAPI.
 * @apiSuccess {Number} date_published Date when news site added the report.
 * @apiSuccess {Number} date_added Date when report was added to SNAPI.
 * @apiParam {Date} published_date Date when news site added the report (full-time representation)
 * @apiParam {Date} imported_date Date when the report was added to SNAPI (full-time representation)
 *
 * @apiSuccessExample Success-Response:
 * HTTP/1.1 200 OK
 * {
 *   "docs": [
 *     {
 *
 *     }
 *   ],
 *   "totalDocs": 719,
 *   "limit": 10,
 *   "hasPrevPage": false,
 *   "hasNextPage": true,
 *   "page": 1,
 *   "totalPages": 72,
 *   "prevPage": null,
 *   "nextPage": 2
 * }
 *
 *
 * @apiErrorExample Error-Response:
 *     HTTP/1.1 400 Bad request
 *     {
 *       "message": "Uh-oh, something went wrong. Please try again!"
 *     }
 */
