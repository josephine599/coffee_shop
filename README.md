# Coffee Shop Project

## Overview

This project models a Coffee Shop using Python and object-oriented programming. It has three main classes: `Customer`, `Coffee`, and `Order`. The system tracks which customers order which coffees, handles prices, and can calculate stats like the most popular coffee or the customer who spends the most.  

---

## Features

- **Customer**
  - Stores customer name (1–15 characters)
  - Keeps track of all orders and coffees bought
  - Can create new orders
  - Has a class method `most_aficionado(coffee)` to find the customer who spent the most on a specific coffee

- **Coffee**
  - Stores coffee name (minimum 3 characters)
  - Keeps track of orders and unique customers
  - Can calculate total orders and average price

- **Order**
  - Connects a `Customer` to a `Coffee` with a price
  - Checks that the price is between 1.0–10.0 and the objects are valid

- **Testing**
  - Uses `pytest` for testing all classes and methods
  - Tests are in the `tests/` folder

- **Debugging**
  - `debug.py` can be used to try out the classes and see how they work together

---


---

## How to Use

1. Activate the virtual environment:

```bash
pipenv shell

python debug.py

pytest


# Clone the repository
git clone https://github.com/josephine599/coffee_shop
cd coffee_shop


