# customer.py

from order import Order  # Import the Order class from the order module

class Customer:
    all = []  # Class variable to keep track of all Customer instances

    def __init__(self, name):
        self.name = name  # Initialize the customer's name
        Customer.all.append(self)  # Add this customer to the all list

    # Property for the customer's name with validation
    @property
    def name(self):
        return self._name  # Return the private name attribute

    @name.setter
    def name(self, value):
        # Validate that the name is a string
        if not isinstance(value, str):
            raise Exception("Customer name must be a string")
        # Validate that the name length is between 1 and 15 characters
        if not (1 <= len(value) <= 15):
            raise Exception("Name must be between 1 and 15 chars")
        self._name = value  # Set the private name attribute

    # Returns all orders for this customer
    def orders(self):
        return [order for order in Order.all if order.customer == self]

    # Returns unique coffees ordered by this customer
    def coffees(self):
        return list({order.coffee for order in self.orders()})

    # Helper method to create an order for this customer
    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """Returns the customer who spent the most on a given coffee"""
        spenders = {}  # Dictionary to track spending per customer
        for order in Order.all:
            if order.coffee == coffee:  # Check if the order is for the specified coffee
                # Update the total spent by the customer
                spenders[order.customer] = spenders.get(order.customer, 0) + order.price

        if not spenders:  # If no spenders found, return None
            return None

        # Return the customer who spent the most
        return max(spenders, key=spenders.get)
