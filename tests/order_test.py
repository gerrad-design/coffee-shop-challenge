import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def test_valid_order(self):
        c = Customer("Zoe")
        coffee = Coffee("Cappuccino")
        order = Order(c, coffee, 4.5)
        self.assertEqual(order.price, 4.5)
        self.assertEqual(order.customer, c)
        self.assertEqual(order.coffee, coffee)

    def test_invalid_price(self):
        c = Customer("Zoe")
        coffee = Coffee("Drip")
        with self.assertRaises(ValueError):
            Order(c, coffee, 15.0)
