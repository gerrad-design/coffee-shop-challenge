import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    def setUp(self):
        Order.all_orders.clear()

    def test_valid_order(self):
        c = Customer("John")
        coffee = Coffee("Latte")
        o = Order(c, coffee, 5.0)
        self.assertEqual(o.customer, c)
        self.assertEqual(o.coffee, coffee)
        self.assertEqual(o.price, 5.0)

    def test_invalid_price(self):
        c = Customer("Jane")
        coffee = Coffee("Espresso")
        with self.assertRaises(ValueError):
            Order(c, coffee, 0.5)

    def test_invalid_customer_type(self):
        coffee = Coffee("Latte")
        with self.assertRaises(TypeError):
            Order("not a customer", coffee, 5.0)

    def test_invalid_coffee_type(self):
        c = Customer("Jane")
        with self.assertRaises(TypeError):
            Order(c, "not a coffee", 5.0)
