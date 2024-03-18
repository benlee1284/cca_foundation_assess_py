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


@pytest.mark.parametrize(
    "product, stock_change_value, expected_stock",
    [
        (GUITAR, 3, 8),
        (GUITAR, -3, 2),
    ],
)
def test_warehouse_adjust_stock(
    product: Product, stock_change_value: int, expected_stock: int
):
    warehouse = Warehouse(catalogue=ENTRIES)
    warehouse.adjust_stock(product, stock_change_value)

    warehouse_stock = warehouse.check_stock(product)
    assert warehouse_stock == expected_stock


def test_warehouse_adjust_stock_not_found():
    warehouse = Warehouse(catalogue=ENTRIES)
    with pytest.raises(ValueError, match="Product not found"):
        warehouse.adjust_stock(STRINGS, 5)


def test_warehouse_adjust_stock_past_zero():
    warehouse = Warehouse(catalogue=ENTRIES)
    with pytest.raises(ValueError, match="Cannot reduce stock below 0"):
        warehouse.adjust_stock(GUITAR, -6)
