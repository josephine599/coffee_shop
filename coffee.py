from order import Order

class Coffee:
    def __init__(self, name: str):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string.")
        value = value.strip()
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = value

    def orders(self):
        return [order for order in Order._all if order.coffee is self]

    def customers(self):
        customers = []
        for order in self.orders():
            if order.customer not in customers:
                customers.append(order.customer)
        return customers

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0.0
        return sum(order.price for order in orders) / len(orders)
