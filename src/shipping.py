import requests as requests

from src.regions.constants import Region
from src.regions.fetch_region import RegionFetcher


UK_ORDER_TOTAL_SHIPPING_CUTOFF = 120.0
EU_ORDER_TOTAL_SHIPPING_CUTOFF = 200.0


def calculate_shipping(
    region_fetcher: RegionFetcher, country: str, order_total: float
) -> float:
    region = region_fetcher(country)

    if region == Region.UK.value:
        if order_total < UK_ORDER_TOTAL_SHIPPING_CUTOFF:
            return 4.99
        return 0.0

    elif region == Region.EU.value:
        if order_total < EU_ORDER_TOTAL_SHIPPING_CUTOFF:
            return 9.99
        return 5.99

    elif region == Region.OTHER.value:
        return 9.99
