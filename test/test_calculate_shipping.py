import pytest

from src.countries import Country
from src.shipping import calculate_shipping

from .common_test_doubles import region_fetcher_test_double


@pytest.mark.parametrize(
    "order_total, expected_shipping",
    [
        (1.0, 4.99),
        (119.99, 4.99),
        (120.00, 0.0),
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
        (1.0, 9.99),
        (199.99, 9.99),
        (200.00, 5.99),
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
