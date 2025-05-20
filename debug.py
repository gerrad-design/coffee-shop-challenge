from customer import Customer
from coffee import Coffee

c1 = Customer("Alice")
c2 = Customer("Bob")
latte = Coffee("Latte")

c1.create_order(latte, 5.0)
c2.create_order(latte, 6.0)
c2.create_order(latte, 2.0)

print("Latte orders:", latte.num_orders())
print("Average price:", latte.average_price())
print("Top spender:", Customer.most_aficionado(latte).name)
