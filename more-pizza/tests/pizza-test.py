import unittest
from pizza import Pizza

class PizzaTest(unittest.TestCase):
    def test_pizza_can_contain_slice(self):
        pizza_a = Pizza(0, 5)
        self.assertEqual(pizza_a.slices, 5)

unittest.main()
