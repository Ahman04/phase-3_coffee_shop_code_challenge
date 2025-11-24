# order.py

class Order:
    # Class variable to store all Order instances
    all = []

    def __init__(self, customer, coffee, price):
        # Import required classes
        from customer import Customer
        from coffee import Coffee

        # Validate that customer is a Customer instance
        if not isinstance(customer, Customer):
            raise Exception("Order must have a valid Customer")

        # Validate that coffee is a Coffee instance
        if not isinstance(coffee, Coffee):
            raise Exception("Order must have a valid Coffee")

        # Validate that price is a number (int or float)
        if not (isinstance(price, float) or isinstance(price, int)):
            raise Exception("Price must be a number")
        
        # Validate that price is within acceptable range
        if not (1.0 <= price <= 10.0):
            raise Exception("Price must be between 1.0 and 10.0")

        # Store validated attributes as private variables
        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

        # Add this order instance to the class-level list
        Order.all.append(self)

    # Property to access customer information
    @property
    def customer(self):
        return self._customer

    # Property to access coffee information
    @property
    def coffee(self):
        return self._coffee

    # Property to access order price
    @property
    def price(self):
        return self._price
