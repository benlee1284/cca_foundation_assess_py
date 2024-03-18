import requests as requests

from src.regions.constants import Regions
from src.regions.fetch_region import fetch_region_from_country


def calculate_shipping(country, order_total):
    region = fetch_region_from_country(country)

    shipping = 0.0

    if region == Regions.UK.value:
        if order_total < 100.0:
            shipping = 4.99

    if region == Regions.EU.value:
        if order_total < 100:
            shipping = 8.99
        else:
            shipping = 4.99

    if region == Regions.OTHER.value:
        shipping = 9.99

    return shipping
