import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        Order.all_orders.clear()

    def test_valid_name(self):
        coffee = Coffee("Latte")
        self.assertEqual(coffee.name, "Latte")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Coffee("A")

    def test_average_price_no_orders(self):
        coffee = Coffee("Mocha")
        self.assertEqual(coffee.average_price(), 0)

    def test_average_price_with_orders(self):
        c = Customer("Joe")
        coffee = Coffee("Drip")
        c.create_order(coffee, 3.0)
        c.create_order(coffee, 5.0)
        self.assertEqual(coffee.average_price(), 4.0)

    def test_customers(self):
        c1 = Customer("Zoe")
        c2 = Customer("Max")
        coffee = Coffee("Cappuccino")
        c1.create_order(coffee, 3.5)
        c2.create_order(coffee, 4.5)
        self.assertEqual(set(coffee.customers()), {c1, c2})
