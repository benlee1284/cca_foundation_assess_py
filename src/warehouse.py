from dataclasses import dataclass

from src.product import Product


@dataclass
class Entry:
    product: Product
    stock: int


@dataclass
class Warehouse:
    catalogue: list[Entry]

    def check_stock(self, product: Product) -> int:
        product_entry = next(
            filter(lambda entry: entry.product == product, self.catalogue), None
        )
        if product_entry is None:
            return 0

        return product_entry.stock
