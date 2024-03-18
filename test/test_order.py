from src.address import Address
from src.order import Order, Item
from src.product import Product


def test_add_items_to_order():
    address = Address(
        house="1",
        street="High Street",
        city="Anytown",
        postcode="12345",
        country="UK",
    )
    order = Order(shipping_address=address, items=[])
    product = Product(id=1, description="Guitar", price=100)
    item = Item(product=product, quantity=5)

    order.add_item(item)
    assert order.items == [item]

    order.add_item(item)
    assert order.items == [item, item]
