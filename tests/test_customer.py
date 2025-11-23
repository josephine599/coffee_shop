import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def setup_function():
    Order._all.clear()

def test_customer_orders_and_coffees():
    alice = Customer("Alice")
    latte = Coffee("Latte")
    capp = Coffee("Cap")

    alice.create_order(latte, 3.0)
    alice.create_order(capp, 4.0)

    assert len(alice.orders()) == 2
    coffees = alice.coffees()
    assert latte in coffees and capp in coffees

def test_most_aficionado():
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")

    alice.create_order(latte, 2.0)  # total 2
    alice.create_order(latte, 3.0)  # total 5
    bob.create_order(latte, 4.5)    # total 4.5

    top = Customer.most_aficionado(latte)
    assert top is alice
