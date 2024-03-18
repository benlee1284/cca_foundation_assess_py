import requests as requests

from src.regions.constants import Regions
from src.regions.fetch_region import RegionFetcher


ORDER_TOTAL_SHIPPING_CUTOFF = 100.0


def calculate_shipping(
    region_fetcher: RegionFetcher, country: str, order_total: float
) -> float:
    region = region_fetcher(country)

    if region == Regions.UK.value:
        if order_total < ORDER_TOTAL_SHIPPING_CUTOFF:
            return 4.99
        return 0.0

    elif region == Regions.EU.value:
        if order_total < ORDER_TOTAL_SHIPPING_CUTOFF:
            return 8.99
        return 4.99

    elif region == Regions.OTHER.value:
        return 9.99
