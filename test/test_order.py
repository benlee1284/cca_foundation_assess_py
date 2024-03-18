import pytest

from src.address import Address
from src.countries import Country
from src.order import Order, Item
from src.product import Product
from src.warehouse import Entry, Warehouse

from .common_test_doubles import region_fetcher_test_double


GUITAR = Product(id=1, description="Guitar", price=100)
AMP = Product(id=2, description="Amplifier", price=50)
STRINGS = Product(id=3, description="Guitar Strings", price=10)

ADDRESS = Address(
    house="1",
    street="High Street",
    city="Anytown",
    postcode="12345",
    country=Country.UNITED_KINGDOM.value,
)


def test_add_items_to_order():
    warehouse = Warehouse(catalogue=[Entry(product=GUITAR, stock=10)])
    address = Address(
        house="1",
        street="High Street",
        city="Anytown",
        postcode="12345",
        country=Country.UNITED_KINGDOM.value,
    )
    order = Order(shipping_address=address, items=[])
    item = Item(product=GUITAR, quantity=5)

    order.add_item(item, warehouse)
    assert order.items == [item]

    order.add_item(item, warehouse)
    assert order.items == [item, item]


def test_add_items_to_order_insufficient_stock():
    warehouse = Warehouse(catalogue=[Entry(product=GUITAR, stock=1)])
    address = Address(
        house="1",
        street="High Street",
        city="Anytown",
        postcode="12345",
        country=Country.UNITED_KINGDOM.value,
    )
    order = Order(shipping_address=address, items=[])
    item = Item(product=GUITAR, quantity=5)

    with pytest.raises(ValueError, match="Insufficient stock"):
        order.add_item(item, warehouse)
    assert order.items == []


@pytest.mark.parametrize(
    "order, expected_total_cost",
    [
        pytest.param(
            Order(shipping_address=ADDRESS, items=[]),
            4.99,
            id="empty-order",
        ),
        pytest.param(
            Order(
                shipping_address=ADDRESS,
                items=[
                    Item(product=GUITAR, quantity=5),
                    Item(product=AMP, quantity=1),
                ],
            ),
            550.0,
            id="multiple-items-free-shipping",
        ),
        pytest.param(
            Order(
                shipping_address=ADDRESS,
                items=[
                    Item(product=AMP, quantity=1),
                    Item(product=STRINGS, quantity=3),
                ],
            ),
            84.99,
            id="multiple-items-plus-shipping",
        ),
    ],
)
def test_calculate_total_cost_of_order(order: Order, expected_total_cost: float):
    result_under_test = order.calculate_total_cost_of_order(
        region_fetcher=region_fetcher_test_double,
    )
    assert result_under_test == expected_total_cost
