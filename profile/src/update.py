import jinja2
import time
import requests
import json
import cv2
import os
import html

LL2_ENDPOINT = "https://ll.thespacedevs.com/2.2.0/launch/upcoming/?mode=detailed&hide_recent_previous=true"
SNAPI_ENDPOINT = "https://api.spaceflightnewsapi.net/v3/articles"
BASE_TIME_URL = "https://www.timeanddate.com/worldclock/fixedtime.html?iso={iso}"
CACHE_DIR = "../cache"
ISO3_JSON = "http://country.io/iso3.json"
BASE_GOOGLE_CALENDAR_URL = "https://www.google.com/calendar/render?action=TEMPLATE&text={text}&location={location}&dates={date1}%2F{date2}"

STATUS_MAP = {"Go": "🟩 ", "TBC": "🟨 ", "TBD": "🟧 ", "Hold": "🟪 "}

# create cache dir if it doesnt exist
os.makedirs(CACHE_DIR, exist_ok=True)


def first_letter_lower(s):
    return s[0].lower() + s[1:]


def status_emoji(status):
    return STATUS_MAP[status]


def make_google_calender_url(launch):
    return BASE_GOOGLE_CALENDAR_URL.format(
        text=html.escape(launch["name"]),
        location=html.escape(launch["pad"]["location"]["name"]),
        date1=time.strftime(
            "%Y%m%dT%H%M%SZ",
            time.strptime(launch["window_start"], "%Y-%m-%dT%H:%M:%SZ"),
        ),
        date2=time.strftime(
            "%Y%m%dT%H%M%SZ", time.strptime(launch["window_end"], "%Y-%m-%dT%H:%M:%SZ")
        ),
    )


def make_google_calender_href_icon(launch):
    """
    create a google calendar href icon
    """
    return f'<a href="{make_google_calender_url(launch)}"><img border="0" width="15" src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Google_Calendar_icon_%282020%29.svg"></a>'


def make_time_and_date_link(timestamp):
    """
    create a link to a time and date
    """
    # convert the timestamp to a string in iso format
    iso = time.strftime("%Y%m%dT%H%M%S", timestamp)
    return BASE_TIME_URL.format(iso=iso)


def get_iso3_to_iso2_country_map():
    """
    get a map from iso3 to iso2
    """
    # get the json
    r = requests.get(ISO3_JSON)
    data = r.json()

    # create a map from iso3 to iso2
    iso3_to_iso2 = {}
    for k, v in data.items():
        iso3_to_iso2[v] = k

    return iso3_to_iso2


def cache_image_and_make_square(url, filename):
    """
    cache an image and make it square from center using PIL
    """
    # get the image
    r = requests.get(url)

    # save image
    with open(filename, "wb") as f:
        f.write(r.content)

    # open the image
    img = cv2.imread(filename)

    # get the image size
    height, width, _ = img.shape

    # get the new size
    new_size = min(height, width)

    # get the center
    center_x = width // 2
    center_y = height // 2

    # get the new image
    new_img = img[
        center_y - new_size // 2 : center_y + new_size // 2,
        center_x - new_size // 2 : center_x + new_size // 2,
    ]

    # save the image
    cv2.imwrite(filename, new_img)
    add_border_to_image(filename)
    return "/".join(filename.split("/")[1:])


ISO3_2_ISO2 = get_iso3_to_iso2_country_map()


def make_datetime_human_readable(timestamp):
    """
    make a timestamp human readable
    """
    # get the timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S UTC", timestamp)
    # timestamp = time.strftime("%B %d, %Y UTC", timestamp)
    return timestamp


def make_markdown_linked_time(timestamp):
    """
    create a link to a time and date
    """
    # convert the timestamp to a string in iso format
    s = make_datetime_human_readable(timestamp)
    url = make_time_and_date_link(timestamp)
    return f"[{s}]({url})"


def make_html_linked_time(timestamp):
    """
    create a link to a time and date
    """
    # convert the timestamp to a string in iso format
    s = make_datetime_human_readable(timestamp)
    url = make_time_and_date_link(timestamp)
    return f'<a href="{url}">{s}</a>'


def get_upcoming_launches(cache_time=3600 // 2):
    """
    get upcoming launches from the Launch Library 2 API
    """
    # check if launches are cached
    # cache launches by the time
    # if cache is older than 1 hour, update cache

    # get the current time
    now = time.time()

    # get the time of the last update from filename
    # if the file does not exist, create it
    try:
        with open(os.path.join(CACHE_DIR, "launches_last_update.txt"), "r") as f:
            last_update = f.read()
    except FileNotFoundError:
        last_update = now

    # if the cache is older than 1 hour, update cache
    if (now - float(last_update) > cache_time) | (last_update == now):
        # get the data from the api
        r = requests.get(LL2_ENDPOINT)
        data = r.json()

        # write the data to the cache
        with open(os.path.join(CACHE_DIR, "launch_cache.json"), "w") as f:
            json.dump(data, f)

        # update the last update time
        with open(os.path.join(CACHE_DIR, "launches_last_update.txt"), "w") as f:
            f.write(str(now))

    # read the cache
    with open(os.path.join(CACHE_DIR, "launch_cache.json"), "r") as f:
        data = json.load(f)

    # return the data
    return data


# def generate_next_launch(data):
#     """
#     generate the next launch readme
#     """
#     # get the template
#
#     # render the template
#     description = """
#
#     """


def inlay_pad_image_in_location_image(pad_image, location_image):
    """
    inlay a pad image in a location image
    """
    # get the pad image
    pad_image = cv2.imread(pad_image)

    # get the location image
    location_image = cv2.imread(location_image)

    # get the pad image size
    pad_height, pad_width, _ = pad_image.shape

    coord1 = (0.525, 0.025)
    coord2 = (0.975, 0.475)

    # resize the location image so closeup fits between (x1,y2) and (x1,y2)
    new_image = cv2.resize(
        location_image,
        (
            int(1 / (coord2[0] - coord1[0]) * pad_width),
            int(1 / (coord2[1] - coord1[1]) * pad_height),
        ),
    )

    # get the location image size
    location_height, location_width, _ = new_image.shape

    # get coordinates in location image for (5% y, 55% x)
    pad_x1 = int(location_width * coord1[0])
    pad_y1 = int(location_height * coord1[1])

    # get coordinates in location image for (45% y, 95% x)
    pad_x2 = int(location_width * coord2[0])
    pad_y2 = int(location_height * coord2[1])

    # get coordinates of center square of new_image
    # frac = 0.01
    # new_image_x1 = int(location_width * (0.5 - frac))
    # new_image_y1 = int(location_height * (0.5 - frac))
    # new_image_x2 = int(location_width * (0.5 + frac))
    # new_image_y2 = int(location_height * (0.5 + frac))

    # draw colorless rectangle with white edges for new image coords
    # new_image = cv2.rectangle(new_image,
    #                           (new_image_x1, new_image_y1),
    #                           (new_image_x2, new_image_y2),
    #                           (255, 255, 255),
    #                           thickness=2)

    # pace pad image into location between coordinates
    new_image[pad_y1:pad_y2, pad_x1:pad_x2] = pad_image

    # # draw line from center of new image to x1,y1
    # cv2.line(new_image, (new_image_x1, new_image_y1), (pad_x1, pad_y1), (255, 255, 255), 2)
    #
    # # draw line from center of new image to x1,y2
    # cv2.line(new_image, (new_image_x2, new_image_y1), (pad_x1, pad_y2), (255, 255, 255), 2)
    #
    # # draw line from center of new image to x2,y2
    # cv2.line(new_image, (new_image_x2, new_image_y2), (pad_x2, pad_y2), (255, 255, 255), 2)

    # return the new pad image
    return new_image


def add_a_an(s):
    if s[0] in "aeiouAEIOU":
        return "an " + s
    else:
        return "a " + s


def parse_launch_windows_to_datetime(launches):
    for launch in launches:
        # get datetime from window_start string
        launch["datetime"] = time.strptime(launch["window_start"], "%Y-%m-%dT%H:%M:%SZ")
    return launches


def get_country_flag_svg(iso3_country_code, country_reassign):
    if iso3_country_code:
        if country_reassign:
            if iso3_country_code == "KAZ":
                iso3_country_code = "RUS"
            elif iso3_country_code == "GUF":
                iso3_country_code = "FRA"
        # convert iso3 to iso2
        iso2_country_code = ISO3_2_ISO2[iso3_country_code]
        return f"https://raw.githubusercontent.com/lipis/flag-icons/main/flags/4x3/{iso2_country_code.lower()}.svg"
    return f"https://upload.wikimedia.org/wikipedia/commons/e/ef/International_Flag_of_Planet_Earth.svg"


def parse_launches_within_a_month(launches):
    upcoming_launches = []
    t_now = time.mktime(time.localtime())
    for i, launch in enumerate(launches):
        t_launch = time.mktime(launch["datetime"])
        if (t_launch > t_now) & (t_launch < t_now + 2592000):
            upcoming_launches.append(launch)
    return upcoming_launches


def add_border_to_image(image_path, border_width_fraction=0.0025):
    white = [255, 255, 255]
    img1 = cv2.imread(image_path)
    height, width, channels = img1.shape
    img2 = cv2.copyMakeBorder(
        img1,
        int(border_width_fraction * height),
        int(border_width_fraction * height),
        int(border_width_fraction * width),
        int(border_width_fraction * width),
        cv2.BORDER_CONSTANT,
        value=white,
    )
    cv2.imwrite(image_path, img2)


# get readme data
def get_readme_data():
    """
    get the readme data for the readme file generation
    """
    # get timestamp and ensure tz is UTC
    # timestamp = time.gmtime()
    # timestamp = time.strftime("%Y-%m-%d %H:%M:%S", timestamp)
    launches = get_upcoming_launches()["results"]
    launches = parse_launch_windows_to_datetime(launches)
    next_launch = launches[0]
    next_launch["cached_location_image"] = cache_image_and_make_square(
        next_launch["pad"]["location"]["map_image"],
        os.path.join(CACHE_DIR, "map_image.png"),
    )
    next_launch["cached_pad_location_image"] = cache_image_and_make_square(
        next_launch["pad"]["map_image"], os.path.join(CACHE_DIR, "map_pad_image.png")
    )
    next_launch["cached_launch_image"] = cache_image_and_make_square(
        next_launch["image"], os.path.join(CACHE_DIR, "launch_image.png")
    )

    new_pad_image = inlay_pad_image_in_location_image(
        "../" + next_launch["cached_pad_location_image"],
        "../" + next_launch["cached_location_image"],
    )
    # save new pad image
    cv2.imwrite(os.path.join(CACHE_DIR, "new_pad_image.png"), new_pad_image)
    next_launch["cached_location_image"] = "profile/cache/new_pad_image.png"
    next_launch["cached_launch_image"] = "profile/cache/launch_image.png"
    latest_news = get_latest_news()
    launch_news = get_launch_news(next_launch["id"])
    if next_launch["mission"] is None:
        next_launch["mission"] = {}
        next_launch["mission"]["name"] = "Unknown Payload"
        next_launch["mission"]["type"] = "Unknown"
        next_launch["mission"]["orbit"] = {}
        next_launch["mission"]["orbit"]["name"] = "Unknown Orbit"
        next_launch["mission"]["orbit"]["abbrev"] = "-"
        next_launch["mission"]["description"] = "Unknown Payload"
    elif next_launch["mission"]["orbit"] is None:
        next_launch["mission"]["orbit"] = {}
        next_launch["mission"]["orbit"]["name"] = "Unknown Orbit"
        next_launch["mission"]["orbit"]["abbrev"] = "-"

    return {
        "timestamp": time.gmtime(),
        "launches": launches,
        "next_launch": next_launch,
        "make_html_linked_time": make_html_linked_time,
        "parse_launches_within_a_month": parse_launches_within_a_month,
        "get_country_flag_svg": get_country_flag_svg,
        "get_iso3_to_iso2_country_map": get_iso3_to_iso2_country_map,
        "status_emoji": status_emoji,
        "first_letter_lower": first_letter_lower,
        "add_a_an": add_a_an,
        "make_google_calender_href_icon": make_google_calender_href_icon,
        "latest_news": latest_news,
        "launch_news": launch_news,
    }


def get_latest_news(cache_time=3600 // 2):
    """
    get the latest news from the Spaceflight News API
    """
    # check if news are cached
    # cache news by the time
    # if cache is older than 1 hour, update cache

    # get the current time
    now = time.time()

    # get the time of the last update from filename
    # if the file does not exist, create it
    try:
        with open(os.path.join(CACHE_DIR, "latest_news_last_update.txt"), "r") as f:
            last_update = f.read()
    except FileNotFoundError:
        last_update = now

    # if the cache is older than 1 hour, update cache
    if (now - float(last_update) > cache_time) | (last_update == now):
        # get the data from the api
        r = requests.get(SNAPI_ENDPOINT + "?_limit=5")
        data = r.json()

        # write the data to the cache
        with open(os.path.join(CACHE_DIR, "latest_news_cache.json"), "w") as f:
            json.dump(data, f)

        # update the last update time
        with open(os.path.join(CACHE_DIR, "latest_news_last_update.txt"), "w") as f:
            f.write(str(now))

    # read the cache
    with open(os.path.join(CACHE_DIR, "latest_news_cache.json"), "r") as f:
        data = json.load(f)

    # return the data
    return data


def get_launch_news(launch_ID, cache_time=3600 // 2):
    """
    get all news related to a launch from the Spaceflight News API
    """
    # check if news are cached
    # cache news by the time
    # if cache is older than 1 hour, update cache

    # get the current time
    now = time.time()

    # get the time of the last update from filename
    # if the file does not exist, create it
    try:
        with open(os.path.join(CACHE_DIR, "launch_news_last_update.txt"), "r") as f:
            last_update = f.read()
    except FileNotFoundError:
        last_update = now

    # if the cache is older than 1 hour, update cache
    if (now - float(last_update) > cache_time) | (last_update == now):
        # get the data from the api
        r = requests.get(SNAPI_ENDPOINT + "/launch/" + launch_ID)
        data = r.json()

        # write the data to the cache
        with open(os.path.join(CACHE_DIR, "launch_news_cache.json"), "w") as f:
            json.dump(data, f)

        # update the last update time
        with open(os.path.join(CACHE_DIR, "launch_news_last_update.txt"), "w") as f:
            f.write(str(now))

    # read the cache
    with open(os.path.join(CACHE_DIR, "launch_news_cache.json"), "r") as f:
        data = json.load(f)

    # return the data
    return data


# load template file
template_loader = jinja2.FileSystemLoader(searchpath="./templates")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template("README.md.j2")

if __name__ == "__main__":
    # # load data
    data = get_readme_data()

    # render template
    output = template.render(**data)

    # write output
    with open(os.path.join("..", "README.md"), "w", encoding="utf-8") as f:
        f.write(output)
