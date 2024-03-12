from datetime import datetime
from enum import Enum
from typing import Any
from uuid import UUID


class TypeEnum(Enum):
    COMMERCIAL = "Commercial"
    GOVERNMENT = "Government"
    MULTINATIONAL = "Multinational"


class LaunchServiceProvider:
    id: int
    url: str
    name: str
    type: TypeEnum

    def __init__(self, id: int, url: str, name: str, type: TypeEnum) -> None:
        self.id = id
        self.url = url
        self.name = name
        self.type = type


class MissionPatch:
    id: int
    name: str
    priority: int
    image_url: str
    agency: LaunchServiceProvider

    def __init__(
        self,
        id: int,
        name: str,
        priority: int,
        image_url: str,
        agency: LaunchServiceProvider,
    ) -> None:
        self.id = id
        self.name = name
        self.priority = priority
        self.image_url = image_url
        self.agency = agency


class LocationEnum(Enum):
    BOCA_CHICA_TEXAS = "Boca Chica, Texas"
    INTERNATIONAL_SPACE_STATION = "International Space Station"
    THE_24000000_KM_FROM_SUN = "24,000,000 km from Sun."


class TypeClass:
    id: int
    name: str

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


class Spacestation:
    id: int
    url: str
    name: LocationEnum
    status: TypeClass
    orbit: str
    image_url: str
    founded: datetime | None
    description: str | None

    def __init__(
        self,
        id: int,
        url: str,
        name: LocationEnum,
        status: TypeClass,
        orbit: str,
        image_url: str,
        founded: datetime | None,
        description: str | None,
    ) -> None:
        self.id = id
        self.url = url
        self.name = name
        self.status = status
        self.orbit = orbit
        self.image_url = image_url
        self.founded = founded
        self.description = description


class Spacewalk:
    id: int
    url: str
    name: str
    start: datetime
    end: datetime
    duration: str
    location: LocationEnum

    def __init__(
        self,
        id: int,
        url: str,
        name: str,
        start: datetime,
        end: datetime,
        duration: str,
        location: LocationEnum,
    ) -> None:
        self.id = id
        self.url = url
        self.name = name
        self.start = start
        self.end = end
        self.duration = duration
        self.location = location


class Expedition:
    id: int
    url: str
    name: str
    start: datetime
    end: datetime
    spacestation: Spacestation
    mission_patches: list[MissionPatch]
    spacewalks: list[Spacewalk]

    def __init__(
        self,
        id: int,
        url: str,
        name: str,
        start: datetime,
        end: datetime,
        spacestation: Spacestation,
        mission_patches: list[MissionPatch],
        spacewalks: list[Spacewalk],
    ) -> None:
        self.id = id
        self.url = url
        self.name = name
        self.start = start
        self.end = end
        self.spacestation = spacestation
        self.mission_patches = mission_patches
        self.spacewalks = spacewalks


class Code(Enum):
    EN = "en"


class Name(Enum):
    ENGLISH = "English"


class Language:
    id: int
    name: Name
    code: Code

    def __init__(self, id: int, name: Name, code: Code) -> None:
        self.id = id
        self.name = name
        self.code = code


class URL:
    priority: int
    source: str
    title: str
    description: str
    feature_image: str | None
    url: str
    type: TypeClass | None
    language: Language

    def __init__(
        self,
        priority: int,
        source: str,
        title: str,
        description: str,
        feature_image: str | None,
        url: str,
        type: TypeClass | None,
        language: Language,
    ) -> None:
        self.priority = priority
        self.source = source
        self.title = title
        self.description = description
        self.feature_image = feature_image
        self.url = url
        self.type = type
        self.language = language


class Status:
    id: int
    name: str
    abbrev: str
    description: str | None

    def __init__(self, id: int, name: str, abbrev: str, description: str | None) -> None:
        self.id = id
        self.name = name
        self.abbrev = abbrev
        self.description = description


class Mission:
    id: int
    name: str
    description: str
    launch_designator: None
    type: str
    orbit: Status
    agencies: list[Any]
    info_urls: list[Any]
    vid_urls: list[Any]

    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        launch_designator: None,
        type: str,
        orbit: Status,
        agencies: list[Any],
        info_urls: list[Any],
        vid_urls: list[Any],
    ) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.launch_designator = launch_designator
        self.type = type
        self.orbit = orbit
        self.agencies = agencies
        self.info_urls = info_urls
        self.vid_urls = vid_urls


class LocationClass:
    id: int
    url: str
    name: str
    country_code: str
    description: None
    map_image: str
    timezone_name: str
    total_launch_count: int
    total_landing_count: int

    def __init__(
        self,
        id: int,
        url: str,
        name: str,
        country_code: str,
        description: None,
        map_image: str,
        timezone_name: str,
        total_launch_count: int,
        total_landing_count: int,
    ) -> None:
        self.id = id
        self.url = url
        self.name = name
        self.country_code = country_code
        self.description = description
        self.map_image = map_image
        self.timezone_name = timezone_name
        self.total_launch_count = total_launch_count
        self.total_landing_count = total_landing_count


class Pad:
    id: int
    url: str
    agency_id: None
    name: str
    description: None
    info_url: None
    wiki_url: str
    map_url: str
    latitude: str
    longitude: str
    location: LocationClass
    country_code: str
    map_image: str
    total_launch_count: int
    orbital_launch_attempt_count: int

    def __init__(
        self,
        id: int,
        url: str,
        agency_id: None,
        name: str,
        description: None,
        info_url: None,
        wiki_url: str,
        map_url: str,
        latitude: str,
        longitude: str,
        location: LocationClass,
        country_code: str,
        map_image: str,
        total_launch_count: int,
        orbital_launch_attempt_count: int,
    ) -> None:
        self.id = id
        self.url = url
        self.agency_id = agency_id
        self.name = name
        self.description = description
        self.info_url = info_url
        self.wiki_url = wiki_url
        self.map_url = map_url
        self.latitude = latitude
        self.longitude = longitude
        self.location = location
        self.country_code = country_code
        self.map_image = map_image
        self.total_launch_count = total_launch_count
        self.orbital_launch_attempt_count = orbital_launch_attempt_count


class Program:
    id: int
    url: str
    name: str
    description: str
    agencies: list[LaunchServiceProvider]
    image_url: str
    start_date: datetime
    end_date: None
    info_url: str | None
    wiki_url: str
    mission_patches: list[Any]

    def __init__(
        self,
        id: int,
        url: str,
        name: str,
        description: str,
        agencies: list[LaunchServiceProvider],
        image_url: str,
        start_date: datetime,
        end_date: None,
        info_url: str | None,
        wiki_url: str,
        mission_patches: list[Any],
    ) -> None:
        self.id = id
        self.url = url
        self.name = name
        self.description = description
        self.agencies = agencies
        self.image_url = image_url
        self.start_date = start_date
        self.end_date = end_date
        self.info_url = info_url
        self.wiki_url = wiki_url
        self.mission_patches = mission_patches


class Configuration:
    id: int
    url: str
    name: str
    family: str
    full_name: str
    variant: str

    def __init__(self, id: int, url: str, name: str, family: str, full_name: str, variant: str) -> None:
        self.id = id
        self.url = url
        self.name = name
        self.family = family
        self.full_name = full_name
        self.variant = variant


class Rocket:
    id: int
    configuration: Configuration

    def __init__(self, id: int, configuration: Configuration) -> None:
        self.id = id
        self.configuration = configuration


class Launch:
    id: UUID
    url: str
    slug: str
    name: str
    status: Status
    last_updated: datetime
    net: datetime
    window_end: datetime
    window_start: datetime
    net_precision: None
    probability: int
    weather_concerns: None
    holdreason: str | None
    failreason: str | None
    hashtag: str | None
    launch_service_provider: LaunchServiceProvider
    rocket: Rocket
    mission: Mission
    pad: Pad
    webcast_live: bool
    image: str
    infographic: None
    program: list[Program]
    orbital_launch_attempt_count: int
    location_launch_attempt_count: int
    pad_launch_attempt_count: int
    agency_launch_attempt_count: int
    orbital_launch_attempt_count_year: int
    location_launch_attempt_count_year: int
    pad_launch_attempt_count_year: int
    agency_launch_attempt_count_year: int

    def __init__(
        self,
        id: UUID,
        url: str,
        slug: str,
        name: str,
        status: Status,
        last_updated: datetime,
        net: datetime,
        window_end: datetime,
        window_start: datetime,
        net_precision: None,
        probability: int,
        weather_concerns: None,
        holdreason: str | None,
        failreason: str | None,
        hashtag: str | None,
        launch_service_provider: LaunchServiceProvider,
        rocket: Rocket,
        mission: Mission,
        pad: Pad,
        webcast_live: bool,
        image: str,
        infographic: None,
        program: list[Program],
        orbital_launch_attempt_count: int,
        location_launch_attempt_count: int,
        pad_launch_attempt_count: int,
        agency_launch_attempt_count: int,
        orbital_launch_attempt_count_year: int,
        location_launch_attempt_count_year: int,
        pad_launch_attempt_count_year: int,
        agency_launch_attempt_count_year: int,
    ) -> None:
        self.id = id
        self.url = url
        self.slug = slug
        self.name = name
        self.status = status
        self.last_updated = last_updated
        self.net = net
        self.window_end = window_end
        self.window_start = window_start
        self.net_precision = net_precision
        self.probability = probability
        self.weather_concerns = weather_concerns
        self.holdreason = holdreason
        self.failreason = failreason
        self.hashtag = hashtag
        self.launch_service_provider = launch_service_provider
        self.rocket = rocket
        self.mission = mission
        self.pad = pad
        self.webcast_live = webcast_live
        self.image = image
        self.infographic = infographic
        self.program = program
        self.orbital_launch_attempt_count = orbital_launch_attempt_count
        self.location_launch_attempt_count = location_launch_attempt_count
        self.pad_launch_attempt_count = pad_launch_attempt_count
        self.agency_launch_attempt_count = agency_launch_attempt_count
        self.orbital_launch_attempt_count_year = orbital_launch_attempt_count_year
        self.location_launch_attempt_count_year = location_launch_attempt_count_year
        self.pad_launch_attempt_count_year = pad_launch_attempt_count_year
        self.agency_launch_attempt_count_year = agency_launch_attempt_count_year


class EventResult:
    id: int
    url: str
    slug: str
    name: str
    updates: list[Any]
    last_updated: datetime
    type: TypeClass
    description: str
    webcast_live: bool
    location: LocationEnum
    news_url: str | None
    video_url: str | None
    info_urls: list[URL]
    vid_urls: list[URL]
    feature_image: str
    date: datetime
    date_precision: None
    duration: None
    agencies: list[Any]
    launches: list[Launch]
    expeditions: list[Expedition]
    spacestations: list[Spacestation]
    program: list[Program]

    def __init__(
        self,
        id: int,
        url: str,
        slug: str,
        name: str,
        updates: list[Any],
        last_updated: datetime,
        type: TypeClass,
        description: str,
        webcast_live: bool,
        location: LocationEnum,
        news_url: str | None,
        video_url: str | None,
        info_urls: list[URL],
        vid_urls: list[URL],
        feature_image: str,
        date: datetime,
        date_precision: None,
        duration: None,
        agencies: list[Any],
        launches: list[Launch],
        expeditions: list[Expedition],
        spacestations: list[Spacestation],
        program: list[Program],
    ) -> None:
        self.id = id
        self.url = url
        self.slug = slug
        self.name = name
        self.updates = updates
        self.last_updated = last_updated
        self.type = type
        self.description = description
        self.webcast_live = webcast_live
        self.location = location
        self.news_url = news_url
        self.video_url = video_url
        self.info_urls = info_urls
        self.vid_urls = vid_urls
        self.feature_image = feature_image
        self.date = date
        self.date_precision = date_precision
        self.duration = duration
        self.agencies = agencies
        self.launches = launches
        self.expeditions = expeditions
        self.spacestations = spacestations
        self.program = program


class EventResponse:
    count: int
    next: str
    previous: None
    results: list[EventResult]

    def __init__(self, count: int, next: str, previous: None, results: list[EventResult]) -> None:
        self.count = count
        self.next = next
        self.previous = previous
        self.results = results
