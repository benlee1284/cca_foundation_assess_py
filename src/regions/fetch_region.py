import requests
from typing import Protocol


class RegionFetcher(Protocol):
    @staticmethod
    def __call__(country: str) -> str: ...


def fetch_region_from_country(country: str) -> str:
    url = (
        "https://npovmrfcyzu2gu42pmqa7zce6a0zikbf.lambda-url.eu-west-2.on.aws/?country="
        + country
    )

    response = requests.get(url)
    response.raise_for_status()

    return response.json()["region"]
