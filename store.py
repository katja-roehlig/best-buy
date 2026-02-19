from products import Product


class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.product_list.append(product)
        else:
            raise TypeError("Only objects of class ‘Product’ allowed!")

    def remove_product(self, product):
        if product in self.product_list:
            self.product_list.remove(product)
        else:
            raise ValueError(f"Your product {product} could not be removed!")

    def get_total_quantity(self) -> int:
        quantity_all_items = 0
        for item in self.product_list:
            quantity = item.get_quantity()
            quantity_all_items += quantity
        return quantity_all_items

    def get_all_products(self) -> list[Product]:
        all_active_products = []
        for item in self.product_list:
            if item.is_active():
                all_active_products.append(item)
        return all_active_products

    def order(self, shopping_list) -> float:
        total_price = 0
        for item, quantity in shopping_list:
            item_price = item.buy(quantity)
            total_price += item_price
        return total_price


def main():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print("Quantity: ", best_buy.get_total_quantity())
    print("Order: ", best_buy.order([(products[0], 1), (products[1], 2)]))


if __name__ == "__main":
    main()
