from products import Product
from store import Store

product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
]


def get_user_choice(prompt, possibilities: list):
    while True:
        try:
            user_action = int(input(prompt))
            if user_action in possibilities:
                return user_action
            else:
                print("Not a valid number!")
                continue
        except ValueError:
            print("That was not a number! Enter a number!")


def start():
    print(
        """
    Store Menu
    ----------
1. List all products in store
2. Show total amount of products in store
3. Make an order
4. Quit 
    """
    )


def handle_order(store):
    available_products = len(store.get_all_products())
    shopping_list = []
    while True:
        while True:
            ordered_product = input(
                f"\nWhen you want to finish order, enter empty text."
                f"\nWhich product do you want(1 - {available_products})? "
            )
            if ordered_product.strip() == "":
                break
            try:
                ordered_product = int(ordered_product)
                ordered_set = set(range(1, available_products + 1))
                if ordered_product in ordered_set:
                    break
                else:
                    print("Not a valid number!")
            except ValueError:
                print("That was not a number! Enter a number!")

        while True:
            ordered_quantity = input("What amount do you want? ")
            if ordered_quantity == "":
                break
            try:
                ordered_quantity = int(ordered_quantity)
                if ordered_quantity > 0:
                    break
                else:
                    print("Not a valid number!")
            except ValueError:
                print("That was not a number! Enter a number!")
        if ordered_product == "" or ordered_quantity == "":
            break
        else:
            index = ordered_product - 1
            list_available_products = store.get_all_products()
            order = list_available_products[index], ordered_quantity
            shopping_list.append(order)
            print("Product added to list!")
            continue
    return shopping_list


def main():
    best_buy = Store(product_list)
    while True:
        start()
        user_choice = get_user_choice("Please choose a number: ", [1, 2, 3, 4])
        if user_choice == 1:
            print()
            for index, item in enumerate(best_buy.get_all_products()):
                print(f"{index + 1}. {item.show()}")
        if user_choice == 2:
            total_items = best_buy.get_total_quantity()
            print(f"\nTotal of {total_items} items in store.")
        if user_choice == 3:
            print()
            for index, item in enumerate(best_buy.get_all_products()):
                print(f"{index + 1}. {item.show()}")
            shopping_list = handle_order(best_buy)
            try:
                total_price = best_buy.order(shopping_list)
                print(f"\nOrder made! Total price: {total_price}")
            except ValueError as e:
                print(f"Error during ordering: {e}")
        if user_choice == 4:
            return


if __name__ == "__main__":
    main()
