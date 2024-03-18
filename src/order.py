from dataclasses import dataclass

from src.address import Address
from src.product import Product
from src.warehouse import Warehouse


@dataclass
class Item:
    product: Product
    quantity: int


@dataclass
class Order:
    shipping_address: Address
    items: list[Item]

    def add_item(self, item: Item, warehouse: Warehouse) -> None:
        stock = warehouse.check_stock(item.product)
        if stock < item.quantity:
            raise ValueError("Insufficient stock")

        self.items.append(item)
