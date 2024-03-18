from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.address import Address
from src.product import Product
from src.regions.fetch_region import RegionFetcher
from src.shipping import calculate_shipping
from src.warehouse import Warehouse

if TYPE_CHECKING:
    from src.history import SalesHistory


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

    def calculate_total_cost_of_order(self, region_fetcher: RegionFetcher) -> float:
        total_cost_of_items = sum(
            item.product.price * item.quantity for item in self.items
        )
        shipping_cost = calculate_shipping(
            region_fetcher=region_fetcher,
            country=self.shipping_address.country,
            order_total=total_cost_of_items,
        )
        return total_cost_of_items + shipping_cost

    def confirm_order(self, warehouse: Warehouse, sales_history: SalesHistory) -> None:
        for item in self.items:
            warehouse.adjust_stock(item.product, item.quantity)

        sales_history.orders.append(self)
