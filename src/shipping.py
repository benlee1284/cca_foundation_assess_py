import requests as requests

from src.regions.constants import Regions
from src.regions.fetch_region import RegionFetcher


ORDER_TOTAL_SHIPPING_CUTOFF = 100.0


def calculate_shipping(
    region_fetcher: RegionFetcher, country: str, order_total: float
) -> float:
    region = region_fetcher(country)

    shipping = 0.0

    if region == Regions.UK.value:
        if order_total < ORDER_TOTAL_SHIPPING_CUTOFF:
            shipping = 4.99

    if region == Regions.EU.value:
        if order_total < ORDER_TOTAL_SHIPPING_CUTOFF:
            shipping = 8.99
        else:
            shipping = 4.99

    if region == Regions.OTHER.value:
        shipping = 9.99

    return shipping
