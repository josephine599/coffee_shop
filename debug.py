from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
alice.create_order(latte, 3.5)
alice.create_order(latte, 4.0)
bob.create_order(latte, 5.0)
alice.create_order(espresso, 2.5)

# Print all orders
print("All orders:", Order._all)

# Print latte orders and customers
print("Latte orders:", latte.orders())
print("Latte customers:", latte.customers())

# Print Alice's coffees
print("Alice coffees:", alice.coffees())

# Print Latte stats
print("Latte average price:", latte.average_price())
print("Most aficionado for Latte:", Customer.most_aficionado(latte))
