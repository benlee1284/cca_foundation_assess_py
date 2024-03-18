from dataclasses import dataclass

from src.product import Product


@dataclass
class Entry:
    product: Product
    stock: int


@dataclass
class Warehouse:
    catalogue: list[Entry]

    def get_product_entry(self, product: Product) -> Entry | None:
        return next(
            filter(lambda entry: entry.product == product, self.catalogue), None
        )

    def check_stock(self, product: Product) -> int:
        product_entry = self.get_product_entry(product)
        if product_entry is None:
            return 0

        return product_entry.stock

    def adjust_stock(self, product: Product, stock_change: int) -> None:
        if stock_change < 0:
            raise ValueError("Stock change must be positive")

        product_entry = self.get_product_entry(product)
        if product_entry is None:
            raise ValueError("Product not found")

        new_stock = product_entry.stock - stock_change
        if new_stock < 0:
            raise ValueError("Cannot reduce stock below 0")

        product_entry.stock = new_stock
