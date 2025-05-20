import unittest
from customer import Customer
from coffee import Coffee
from order import Order
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coffee import Coffee 


class TestCustomer(unittest.TestCase):
    def setUp(self):
        Order.all_orders.clear()

    def test_valid_name(self):
        c = Customer("Alice")
        self.assertEqual(c.name, "Alice")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Customer("")

    def test_create_order(self):
        c = Customer("Bob")
        coffee = Coffee("Latte")
        o = c.create_order(coffee, 5.0)
        self.assertIn(o, c.orders())

    def test_coffees(self):
        c = Customer("Dana")
        coffee1 = Coffee("Mocha")
        coffee2 = Coffee("Espresso")
        c.create_order(coffee1, 5.0)
        c.create_order(coffee2, 6.0)
        self.assertEqual(set(c.coffees()), {coffee1, coffee2})

    def test_most_aficionado(self):
        c1 = Customer("A")
        c2 = Customer("B")
        coffee = Coffee("Flat White")
        c1.create_order(coffee, 5.0)
        c2.create_order(coffee, 6.0)
        c2.create_order(coffee, 2.5)
        self.assertEqual(Customer.most_aficionado(coffee), c2)
