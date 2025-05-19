class Order:
    def __init__(self, customer, coffee, price):
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        if not isinstance(customer, object) or not isinstance(coffee, object):
            raise TypeError("Order must be associated with valid Customer and Coffee instances.")
        self._customer = customer
        self._coffee = coffee
        self._price = price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
