from src.countries import Country
from src.regions.constants import Regions


def region_fetcher_test_double(country: str) -> str:
    if country == Country.UNITED_KINGDOM.value:
        return Regions.UK.value
    elif country == Country.FRANCE.value:
        return Regions.EU.value
    elif country == Country.ALBANIA.value:
        return Regions.OTHER.value
    else:
        raise NotImplementedError(f"Country {country} not implemented")

