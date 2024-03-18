from dataclasses import dataclass

from src.address import Address
from src.order import Order
from src.product import Product


@dataclass
class SalesHistory:
    orders: list[Order]

    def list_orders_for_product(self, product: Product) -> list[Order]:
        orders_containing_product = [
            order
            for order in self.orders
            if any(item.product == product for item in order.items)
        ]

        filtered_orders = []

        for order in orders_containing_product:
            relevant_items = [item for item in order.items if item.product == product]
            order_with_only_relevant_items = Order(
                region_fetcher=order.region_fetcher,
                shipping_address=order.shipping_address,
                items=relevant_items,
            )

            filtered_orders.append(order_with_only_relevant_items)

        return filtered_orders

    def list_orders_for_address(self, address: Address) -> list[Order]:
        return [order for order in self.orders if order.shipping_address == address]
