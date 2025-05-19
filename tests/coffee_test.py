import unittest
from customer import Customer
from coffee import Coffee

class TestCoffee(unittest.TestCase):
    def test_valid_name(self):
        coffee = Coffee("Latte")
        self.assertEqual(coffee.name, "Latte")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Coffee("A")

    def test_average_price_no_orders(self):
        coffee = Coffee("Mocha")
        self.assertEqual(coffee.average_price(), 0)
