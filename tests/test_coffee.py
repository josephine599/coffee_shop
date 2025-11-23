import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def setup_function():
    Order._all.clear()

def test_coffee_orders_customers_stats():
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")

    alice.create_order(latte, 2.0)
    bob.create_order(latte, 6.0)

    assert latte.num_orders() == 2
    customers = latte.customers()
    assert alice in customers and bob in customers
    assert round(latte.average_price(), 6) == pytest.approx((2.0 + 6.0) / 2)
