from order import Order  # to access Order._all
from coffee import Coffee

class Customer:
    def __init__(self, name: str):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        value = value.strip()
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        return [order for order in Order._all if order.customer is self]

    def coffees(self):
        coffees = []
        for order in self.orders():
            if order.coffee not in coffees:
                coffees.append(order.coffee)
        return coffees

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        highest_spender = None
        highest_amount = 0

        for order in Order._all:
            if order.coffee is coffee:
                total = sum(o.price for o in Order._all if o.customer is order.customer and o.coffee is coffee)

                if total > highest_amount:
                    highest_amount = total
                    highest_spender = order.customer

        return highest_spender
