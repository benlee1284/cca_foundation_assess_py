import pytest

from src.countries import Country
from src.regions.constants import Regions
from src.shipping import calculate_shipping


def region_fetcher_test_double(country: str) -> str:
    if country == Country.UNITED_KINGDOM.value:
        return Regions.UK.value
    elif country == Country.FRANCE.value:
        return Regions.EU.value
    elif country == Country.ALBANIA.value:
        return Regions.OTHER.value
    else:
        raise NotImplementedError(f"Country {country} not implemented")


@pytest.mark.parametrize(
    "order_total, expected_shipping",
    [
        (1.0, 4.99),
        (99.99, 4.99),
        (100.00, 0.0),
    ],
)
def test_calculate_shipping_uk(order_total: float, expected_shipping: float):
    shipping = calculate_shipping(
        region_fetcher=region_fetcher_test_double,
        country=Country.UNITED_KINGDOM.value,
        order_total=order_total,
    )
    assert shipping == expected_shipping


@pytest.mark.parametrize(
    "order_total, expected_shipping",
    [
        (1.0, 8.99),
        (99.99, 8.99),
        (100.00, 4.99),
    ],
)
def test_calculate_shipping_eu(order_total: float, expected_shipping: float):
    shipping = calculate_shipping(
        region_fetcher=region_fetcher_test_double,
        country=Country.FRANCE.value,
        order_total=order_total,
    )
    assert shipping == expected_shipping


@pytest.mark.parametrize(
    "order_total, expected_shipping",
    [
        (1.0, 9.99),
        (99.99, 9.99),
        (100.00, 9.99),
    ],
)
def test_calculate_shipping_other(order_total: float, expected_shipping: float):
    shipping = calculate_shipping(
        region_fetcher=region_fetcher_test_double,
        country=Country.ALBANIA.value,
        order_total=order_total,
    )
    assert shipping == expected_shipping
