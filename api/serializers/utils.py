from typing import TypedDict


class ClientOptions(TypedDict):
    base_url: str
    headers: dict[str, str]
    timeout: float
