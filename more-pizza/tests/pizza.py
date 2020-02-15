class Pizza:
    def __init__(self, index, slices):
        self.index = index
        self.slices = slices

class PizzaCalculator:
    @classmethod
    def get_ordered_pizza_index(cls, pizza_types, target_slice):
        [list_of_sum_of_pizza_slices, backtrack_pizza_type] = PizzaCalculator.get_sum_pizza_slices(pizza_types, target_slice)
        max_pizza_slice = list_of_sum_of_pizza_slices[-1]
        pizza_index = PizzaCalculator.get_list_of_ordered_pizza_index(max_pizza_slice, backtrack_pizza_type)
        return pizza_index

    @classmethod
    def get_sum_pizza_slices(cls, pizza_types, target_slice):
        list_of_sum_of_pizza_slices = [0]
        backtrack_pizza_type = {}
        for p in pizza_types:
            # print(str(p.index) + " " + str(p.slices))
            new_slices = []
            for sum_slice in list_of_sum_of_pizza_slices:
                new_sum_slice = sum_slice + p.slices
                
                if new_sum_slice < target_slice and new_sum_slice not in list_of_sum_of_pizza_slices:
                    backtrack_pizza_type[new_sum_slice] = p
                    new_slices.append(new_sum_slice)

            list_of_sum_of_pizza_slices.extend(new_slices)

        return [list_of_sum_of_pizza_slices, backtrack_pizza_type]

    @classmethod
    def get_list_of_ordered_pizza_index(cls, pizza_slice, backtrack_pizza_type):
        if pizza_slice not in backtrack_pizza_type:
            return []
        
        pizza_index = str(backtrack_pizza_type[pizza_slice].index)
        new_pizza_slice = pizza_slice - backtrack_pizza_type[pizza_slice].slices
        return PizzaCalculator.get_list_of_ordered_pizza_index(new_pizza_slice, backtrack_pizza_type) + [pizza_index]

if __name__ == '__main__':
    target_slice = 17
    n_pizza = 4
    pizza_types = [
        Pizza(0, 2),
        Pizza(1, 5),
        Pizza(2, 6),
        Pizza(3, 8)
    ]

    pizza_index = PizzaCalculator.get_pizza(pizza_types, target_slice)
    print(len(pizza_index))
    print(", ".join(pizza_index))
