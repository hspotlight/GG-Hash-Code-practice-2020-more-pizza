import unittest
from pizza import Pizza, PizzaCalculator

class PizzaCalculatorTest(unittest.TestCase):
    def test_should_return_pizza_index_0_2_3(self):
        target_slice = 17
        n_pizza = 4
        pizza_types = [
            Pizza(0, 2),
            Pizza(1, 5),
            Pizza(2, 6),
            Pizza(3, 8)
        ]
        pizza_index = PizzaCalculator.get_pizza(pizza_types, target_slice)
        self.assertEqual(3, len(pizza_index))
        self.assertEqual("0, 2, 3", ", ".join(pizza_index))

unittest.main()
