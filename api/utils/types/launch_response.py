from datetime import datetime
from enum import Enum
from typing import Any
from uuid import UUID


class LaunchServiceProviderName(Enum):
    ARMY_BALLISTIC_MISSILE_AGENCY = "Army Ballistic Missile Agency"
    SOVIET_SPACE_PROGRAM = "Soviet Space Program"
    US_NAVY = "US Navy"


class LaunchServiceProviderType(Enum):
    GOVERNMENT = "Government"


class LaunchServiceProvider:
    id: int
    url: str
    name: LaunchServiceProviderName
    type: LaunchServiceProviderType

    def __init__(
        self,
        id: int,
        url: str,
        name: LaunchServiceProviderName,
        type: LaunchServiceProviderType,
    ) -> None:
        self.id = id
        self.url = url
        self.name = name
        self.type = type


class Abbrev(Enum):
    ELLIPTICAL = "Elliptical"
    FAILURE = "Failure"
    LEO = "LEO"
    SUCCESS = "Success"


class StatusName(Enum):
    ELLIPTICAL_ORBIT = "Elliptical Orbit"
    LAUNCH_FAILURE = "Launch Failure"
    LAUNCH_SUCCESSFUL = "Launch Successful"
    LOW_EARTH_ORBIT = "Low Earth Orbit"


class Status:
    id: int
    name: StatusName
    abbrev: Abbrev
    description: str | None

    def __init__(
        self, id: int, name: StatusName, abbrev: Abbrev, description: str | None
    ) -> None:
        self.id = id
        self.name = name
        self.abbrev = abbrev
        self.description = description


class MissionType(Enum):
    EARTH_SCIENCE = "Earth Science"
    TEST_FLIGHT = "Test Flight"


class Mission:
    id: int
    name: str
    description: str
    launch_designator: None
    type: MissionType
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
        type: MissionType,
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


class CountryCode(Enum):
    KAZ = "KAZ"
    USA = "USA"


class LocationName(Enum):
    BAIKONUR_COSMODROME_REPUBLIC_OF_KAZAKHSTAN = (
        "Baikonur Cosmodrome, Republic of Kazakhstan"
    )
    CAPE_CANAVERAL_FL_USA = "Cape Canaveral, FL, USA"


class TimezoneName(Enum):
    AMERICA_NEW_YORK = "America/New_York"
    ASIA_QYZYLORDA = "Asia/Qyzylorda"


class Location:
    id: int
    url: str
    name: LocationName
    country_code: CountryCode
    description: None
    map_image: str
    timezone_name: TimezoneName
    total_launch_count: int
    total_landing_count: int

    def __init__(
        self,
        id: int,
        url: str,
        name: LocationName,
        country_code: CountryCode,
        description: None,
        map_image: str,
        timezone_name: TimezoneName,
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


class PadName(Enum):
    LAUNCH_COMPLEX_18_A = "Launch Complex 18A"
    LAUNCH_COMPLEX_26_A = "Launch Complex 26A"
    THE_15 = "1/5"


class Pad:
    id: int
    url: str
    agency_id: int | None
    name: PadName
    description: None
    info_url: None
    wiki_url: str
    map_url: str
    latitude: str
    longitude: str
    location: Location
    country_code: CountryCode
    map_image: str
    total_launch_count: int
    orbital_launch_attempt_count: int

    def __init__(
        self,
        id: int,
        url: str,
        agency_id: int | None,
        name: PadName,
        description: None,
        info_url: None,
        wiki_url: str,
        map_url: str,
        latitude: str,
        longitude: str,
        location: Location,
        country_code: CountryCode,
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


class Family(Enum):
    REDSTONE = "Redstone"
    SPUTNIK = "Sputnik"
    VANGUARD = "Vanguard"


class Configuration:
    id: int
    url: str
    name: str
    family: Family
    full_name: str
    variant: str

    def __init__(
        self, id: int, url: str, name: str, family: Family, full_name: str, variant: str
    ) -> None:
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


class LaunchResult:
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
    probability: None
    weather_concerns: None
    holdreason: None
    failreason: None
    hashtag: None
    launch_service_provider: LaunchServiceProvider
    rocket: Rocket
    mission: Mission
    pad: Pad
    webcast_live: bool
    image: str | None
    infographic: None
    program: list[Any]
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
        probability: None,
        weather_concerns: None,
        holdreason: None,
        failreason: None,
        hashtag: None,
        launch_service_provider: LaunchServiceProvider,
        rocket: Rocket,
        mission: Mission,
        pad: Pad,
        webcast_live: bool,
        image: str | None,
        infographic: None,
        program: list[Any],
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


class LaunchResponse:
    count: int
    next: str
    previous: None
    results: list[LaunchResult]

    def __init__(
        self, count: int, next: str, previous: None, results: list[LaunchResult]
    ) -> None:
        self.count = count
        self.next = next
        self.previous = previous
        self.results = results
