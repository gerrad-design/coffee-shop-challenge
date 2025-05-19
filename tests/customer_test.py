import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def test_valid_customer_name(self):
        c = Customer("Alice")
        self.assertEqual(c.name, "Alice")

    def test_invalid_customer_name(self):
        with self.assertRaises(ValueError):
            Customer("A" * 20)

    def test_create_order(self):
        c = Customer("Bob")
        coffee = Coffee("Espresso")
        order = c.create_order(coffee, 3.5)
        self.assertEqual(order.price, 3.5)
        self.assertIn(order, c.orders())
