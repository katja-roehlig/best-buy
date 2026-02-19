class Product:
    def __init__(self, name, price, quantity):
        if not name.strip():
            raise ValueError("Productname cannot be empty.")
        if not isinstance(price, (int, float)):
            raise ValueError("Price has to be a number.")
        if price <= 0:
            raise ValueError("Price cannot be 0 or negative.")

        self.validate_quantity(quantity)
        self._name = name
        self._price = price
        self._quantity = quantity
        self._activate = True

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        self.validate_quantity(quantity)
        self._quantity += quantity

    def is_active(self):
        return self._activate

    def activate(self):
        self._activate = True

    def deactivate(self):
        self._activate = False

    def show(self):
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity} "

    def buy(self, quantity) -> float:
        self.validate_quantity(quantity)
        if self._quantity >= quantity:
            total_price = self._price * quantity
            if self._quantity - quantity <= 0:
                self.deactivate()
                self._quantity = 0
            else:
                self._quantity = self._quantity - quantity
        else:
            raise ValueError(f"Not enough products for '{self._name}' available")
        return total_price

    @staticmethod
    def validate_quantity(quantity):
        if not isinstance(quantity, (int)):
            raise ValueError("Quantity has to be an integer.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
