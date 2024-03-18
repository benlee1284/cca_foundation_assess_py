import pytest

from src.product import Product
from src.warehouse import Entry, Warehouse

GUITAR = Product(id=1, description="Guitar", price=100)
AMP = Product(id=2, description="Amplifier", price=50)
STRINGS = Product(id=3, description="Guitar Strings", price=10)


ENTRIES = [
    Entry(GUITAR, 5),
    Entry(AMP, 0),
]


@pytest.mark.parametrize(
    "product, expected_stock",
    [
        (GUITAR, 5),
        (AMP, 0),
        (STRINGS, 0),
    ],
)
def test_warehouse_check_stock(product: Product, expected_stock: int):
    warehouse = Warehouse(catalogue=ENTRIES)
    warehouse_stock = warehouse.check_stock(product)

    assert warehouse_stock == expected_stock
