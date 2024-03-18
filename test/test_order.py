from src.address import Address
from src.order import Order, Item
from src.product import Product
from src.warehouse import Entry, Warehouse


GUITAR = Product(id=1, description="Guitar", price=100)


def test_add_items_to_order():
    warehouse = Warehouse(catalogue=[Entry(product=GUITAR, stock=10)])
    address = Address(
        house="1",
        street="High Street",
        city="Anytown",
        postcode="12345",
        country="UK",
    )
    order = Order(shipping_address=address, items=[])
    item = Item(product=GUITAR, quantity=5)

    order.add_item(item, warehouse)
    assert order.items == [item]

    order.add_item(item, warehouse)
    assert order.items == [item, item]
