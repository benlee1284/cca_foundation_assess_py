from dataclasses import dataclass

import pytest

from src.address import Address
from src.countries import Country
from src.history import SalesHistory
from src.order import Item, Order
from src.product import Product


GUITAR = Product(id=1, description="Guitar", price=100)
AMP = Product(id=2, description="Amplifier", price=50)
STRINGS = Product(id=3, description="Guitar Strings", price=10)

ADDRESS_1 = Address(
    house="1",
    street="High Street",
    city="Anytown",
    postcode="12345",
    country=Country.UNITED_KINGDOM,
)
ADDRESS_2 = Address(
    house="2",
    street="Main Street",
    city="Othertown",
    postcode="12345",
    country=Country.UNITED_KINGDOM,
)


@dataclass
class OrdersTestParam:
    orders: list[Order]
    expected_orders: list[Order]


@pytest.mark.parametrize(
    "orders_param",
    [
        pytest.param(OrdersTestParam(orders=[], expected_orders=[]), id="empty"),
        pytest.param(
            OrdersTestParam(
                orders=[
                    Order(
                        shipping_address=ADDRESS_1,
                        items=[Item(product=GUITAR, quantity=5)],
                    ),
                ],
                expected_orders=[
                    Order(
                        shipping_address=ADDRESS_1,
                        items=[Item(product=GUITAR, quantity=5)],
                    ),
                ],
            ),
            id="single-order-single-item",
        ),
        pytest.param(
            OrdersTestParam(
                orders=[
                    Order(
                        shipping_address=ADDRESS_1,
                        items=[
                            Item(product=GUITAR, quantity=5),
                            Item(product=AMP, quantity=1),
                        ],
                    ),
                ],
                expected_orders=[
                    Order(
                        shipping_address=ADDRESS_1,
                        items=[Item(product=GUITAR, quantity=5)],
                    ),
                ],
            ),
            id="single-order-mutliple-items",
        ),
        pytest.param(
            OrdersTestParam(
                orders=[
                    Order(
                        shipping_address=ADDRESS_1,
                        items=[
                            Item(product=GUITAR, quantity=5),
                            Item(product=AMP, quantity=1),
                        ],
                    ),
                    Order(
                        shipping_address=ADDRESS_1,
                        items=[Item(product=STRINGS, quantity=2)],
                    ),
                    Order(
                        shipping_address=ADDRESS_2,
                        items=[Item(product=GUITAR, quantity=3)],
                    ),
                ],
                expected_orders=[
                    Order(
                        shipping_address=ADDRESS_1,
                        items=[Item(product=GUITAR, quantity=5)],
                    ),
                    Order(
                        shipping_address=ADDRESS_2,
                        items=[Item(product=GUITAR, quantity=3)],
                    ),
                ],
            ),
            id="multiple-orders",
        ),
    ],
)
def test_list_orders_for_product(orders_param: OrdersTestParam):
    sales_history = SalesHistory(orders=orders_param.orders)
    assert sales_history.list_orders_for_product(GUITAR) == orders_param.expected_orders
