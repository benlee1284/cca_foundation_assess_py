import pytest

from src.product import Product
from src.warehouse import Entry, Warehouse

GUITAR = Product(id=1, description="Guitar", price=100)
AMP = Product(id=2, description="Amplifier", price=50)
STRINGS = Product(id=3, description="Guitar Strings", price=10)


@pytest.fixture(scope="function")
def entries() -> list[Entry]:
    return [
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
def test_warehouse_check_stock(
    entries: list[Entry], product: Product, expected_stock: int
):
    warehouse = Warehouse(catalogue=entries)
    warehouse_stock = warehouse.check_stock(product)

    assert warehouse_stock == expected_stock


def test_warehouse_adjust_stock(entries: list[Entry]):
    stock_change_value = 3
    expected_stock = 2
    product = GUITAR

    warehouse = Warehouse(catalogue=entries)
    warehouse.adjust_stock(product, stock_change_value)

    warehouse_stock = warehouse.check_stock(product)
    assert warehouse_stock == expected_stock


def test_warehouse_adjust_stock_not_found(entries: list[Entry]):
    warehouse = Warehouse(catalogue=entries)
    with pytest.raises(ValueError, match="Product not found"):
        warehouse.adjust_stock(STRINGS, 5)


def test_warehouse_adjust_stock_past_zero(entries: list[Entry]):
    warehouse = Warehouse(catalogue=entries)
    with pytest.raises(ValueError, match="Cannot reduce stock below 0"):
        warehouse.adjust_stock(GUITAR, 6)


def test_warehouse_adjust_stock_negative_change(entries: list[Entry]):
    warehouse = Warehouse(catalogue=entries)
    with pytest.raises(ValueError, match="Stock change must be positive"):
        warehouse.adjust_stock(GUITAR, -1)


def test_warehouse_receive_stock_product_entry_doesnt_exist():
    warehouse = Warehouse(catalogue=[])
    product_entry = Entry(product=GUITAR, stock=10)

    warehouse.receive_stock(product=product_entry.product, stock=product_entry.stock)

    assert warehouse.catalogue == [product_entry]


def test_warehouse_receive_stock_product_entry_already_exists():
    product_entry = Entry(product=GUITAR, stock=10)
    warehouse = Warehouse(catalogue=[product_entry])

    additional_stock = 5

    warehouse.receive_stock(product=product_entry.product, stock=additional_stock)

    assert warehouse.catalogue == [Entry(product=GUITAR, stock=15)]
