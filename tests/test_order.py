import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def setup_function():
    Order._all.clear()

def test_order_properties():
    c = Customer("Ann")
    k = Coffee("Mocha")
    o = Order(c, k, 3.0)
    assert o.customer is c
    assert o.coffee is k
    assert isinstance(o.price, float)

    with pytest.raises(ValueError):
        Order(c, k, 0.5)  # invalid price

    with pytest.raises(TypeError):
        Order("not a customer", k, 2.0)
