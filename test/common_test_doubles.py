from src.countries import Country
from src.regions.constants import Region


def region_fetcher_test_double(country: str) -> str:
    if country == Country.UNITED_KINGDOM.value:
        return Region.UK.value
    elif country == Country.FRANCE.value:
        return Region.EU.value
    elif country == Country.ALBANIA.value:
        return Region.OTHER.value
    else:
        raise NotImplementedError(f"Country {country} not implemented")
