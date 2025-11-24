from customer import Customer
from coffee import Coffee
from order import Order

# create customer instances
c1 = Customer("Ali")
c2 = Customer("Mary")

# create coffee types (mocha left unused here but available)
latte = Coffee("Latte")
mocha = Coffee("Mocha")

# customers create orders for the latte with given prices
c1.create_order(latte, 2.0)
c1.create_order(latte, 6.0)
c2.create_order(latte, 4.0)

# display stats for the latte coffee
print("Latte orders:", latte.num_orders())         # number of latte orders
print("Latte avg price:", latte.average_price())   # average price of latte orders
print("Most aficionado:", Customer.most_aficionado(latte).name)  # customer with most latte orders
