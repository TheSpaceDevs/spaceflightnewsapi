import jinja2
import time
import requests
import os
from typing import List, Dict

LL2_LAUNCH_ENDPOINT = "https://ll.thespacedevs.com/2.2.0/launch/?mode=list&limit=100"
LL2_EVENT_ENDPOINT = "https://ll.thespacedevs.com/2.2.0/event/?mode=list&limit=100"
SNAPI_ARTICLES_ENDPOINT = "https://api.spaceflightnewsapi.net/v4/articles"
SNAPI_BLOGS_ENDPOINT = "https://api.spaceflightnewsapi.net/v4/blogs"
SNAPI_INFO_ENDPOINT = "https://api.spaceflightnewsapi.net/v4/info"
BASE_TIME_URL = "https://www.timeanddate.com/worldclock/fixedtime.html?iso={iso}"
CACHE_DIR = "../cache"

# create cache dir if it doesnt exist
os.makedirs(CACHE_DIR, exist_ok=True)


def make_time_and_date_link(timestamp):
    """
    create a link to a time and date
    """
    # convert the timestamp to a string in iso format
    iso = time.strftime("%Y%m%dT%H%M%S", timestamp)
    return BASE_TIME_URL.format(iso=iso)


def make_datetime_human_readable(timestamp):
    """
    make a timestamp human readable
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S UTC", timestamp)
    return timestamp


def make_html_linked_time(timestamp):
    """
    create a link to a time and date
    """
    # convert the timestamp to a string in iso format
    s = make_datetime_human_readable(timestamp)
    url = make_time_and_date_link(timestamp)
    return f'<a href="{url}">{s}</a>'


def get_launches(IDs: List[str]) -> List[Dict]:
    """
    Get the launches from the Launch Library 2 API.
    """
    query_url = LL2_LAUNCH_ENDPOINT + "&id=" + ",".join(IDs)
    r = requests.get(query_url).json()
    launches = r["results"]
    while r["next"]:
        print("paginating launches")
        r = requests.get(r["next"]).json()
        launches += r["results"]
    return launches


def get_events(IDs: List[int]) -> List[Dict]:
    """
    Get the events from the Launch Library 2 API.
    """
    query_url = LL2_EVENT_ENDPOINT + "&id=" + ",".join([str(ID) for ID in IDs])
    r = requests.get(query_url).json()
    events = r["results"]
    while r["next"]:
        print("paginating events")
        r = requests.get(r["next"]).json()
        events += r["results"]
    return events


def link_launches_events(
    objects: List[Dict], launches: List[Dict], events: List[Dict]
) -> List[Dict]:
    for ii, obj in enumerate(objects):
        if obj["launches"]:
            launch_IDs = [launch["launch_id"] for launch in obj["launches"]]
            obj["ll2_launches"] = [
                launch for launch in launches if launch["id"] in launch_IDs
            ]
        objects[ii] = obj
    for ii, obj in enumerate(objects):
        if obj["events"]:
            event_IDs = [event["event_id"] for event in obj["events"]]
            obj["ll2_events"] = [event for event in events if event["id"] in event_IDs]
        objects[ii] = obj
    return objects


def get_latest_articles_blogs() -> (List[Dict], List[Dict]):
    """
    Get the latest articles from the Spaceflight News API.
    """

    # Get the latest articles and blogs from the Spaceflight News API
    r_articles = requests.get(SNAPI_ARTICLES_ENDPOINT + "?_limit=10")
    articles = r_articles.json()["results"]
    r_blogs = requests.get(SNAPI_BLOGS_ENDPOINT + "?_limit=10")
    blogs = r_blogs.json()["results"]

    # Get the LL2 IDs of the launches and events in the articles and blogs
    ll2_launch_IDs = []
    ll2_event_IDs = []
    for article in articles:
        if article["launches"]:
            ll2_launch_IDs += [
                launch["launch_id"]
                for launch in article["launches"]
                if launch["provider"] == "Launch Library 2"
            ]
        if article["events"]:
            ll2_event_IDs += [
                event["event_id"]
                for event in article["events"]
                if event["provider"] == "Launch Library 2"
            ]
    for blog in blogs:
        if blog["launches"]:
            ll2_launch_IDs += [
                launch["launch_id"]
                for launch in blog["launches"]
                if launch["provider"] == "Launch Library 2"
            ]
        if blog["events"]:
            ll2_event_IDs += [
                event["event_id"]
                for event in blog["events"]
                if event["provider"] == "Launch Library 2"
            ]

    # Remove duplicates
    ll2_launch_IDs = list(set(ll2_launch_IDs))
    ll2_event_IDs = list(set(ll2_event_IDs))

    # Get the launches and events from the LL2 API
    launches = get_launches(ll2_launch_IDs)
    events = get_events(ll2_event_IDs)

    # Link the info from launches and events to the articles and blogs
    articles = link_launches_events(articles, launches, events)
    blogs = link_launches_events(blogs, launches, events)

    return articles, blogs


def get_snapi_info() -> dict:
    """
    Get the latest Spaceflight News API info.
    """
    r = requests.get(SNAPI_INFO_ENDPOINT)
    return r.json()


def get_readme_data():
    """
    Get the data for the README file generation.
    """
    snapi_info = get_snapi_info()
    news_sites = snapi_info["news_sites"]
    snapi_version = snapi_info["version"]

    articles, blogs = get_latest_articles_blogs()

    return {
        "timestamp": make_html_linked_time(time.gmtime()),
        "news_sites": news_sites,
        "snapi_version": snapi_version,
        "articles": articles,
        "blogs": blogs,
    }


# load template file
template_loader = jinja2.FileSystemLoader(searchpath=".")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template("template.j2")

if __name__ == "__main__":
    # # load data
    data = get_readme_data()

    # render template
    output = template.render(**data)

    # write output
    with open(os.path.join("../..", "README.md"), "w", encoding="utf-8") as f:
        f.write(output)
