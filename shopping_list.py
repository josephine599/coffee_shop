class ShoppingList:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items
