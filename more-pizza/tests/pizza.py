class Pizza:
    def __init__(self, position, slices):
        self.position = position
        self.slices = slices

def get_sum_pizza_slices(pizza_types, target_slice):
    sum_of_pizza_slices = [0]
    backtrack_pizza_type = {}
    for p in pizza_types:
        # print(str(p.position) + " " + str(p.slices))
        new_slices = []
        for sum_slice in sum_of_pizza_slices:
            new_sum_slice = sum_slice + p.slices
            
            if new_sum_slice < target_slice and new_sum_slice not in sum_of_pizza_slices:
                backtrack_pizza_type[new_sum_slice] = p
                new_slices.append(new_sum_slice)

        sum_of_pizza_slices.extend(new_slices)

    return [sum_of_pizza_slices, backtrack_pizza_type]

def get_ordered_pizza(pizza_slice, backtrack_pizza_type):
    if pizza_slice not in backtrack_pizza_type:
        return []
    
    pizza_position = str(backtrack_pizza_type[pizza_slice].position)
    new_pizza_slice = pizza_slice - backtrack_pizza_type[pizza_slice].slices
    return get_ordered_pizza(new_pizza_slice, backtrack_pizza_type) + [pizza_position]

if __name__ == '__main__':
    target_slice = 17
    n_pizza = 4
    # 0, 2, 3
    # 2, 6, 8
    pizza_types = [
        Pizza(0, 2),
        Pizza(1, 5),
        Pizza(2, 6),
        Pizza(3, 8)
    ]

    [sum_of_pizza_slices, backtrack_pizza_type] = get_sum_pizza_slices(pizza_types, target_slice)
    max_pizza_slice = sum_of_pizza_slices[-1]

    pizza_index = get_ordered_pizza(max_pizza_slice, backtrack_pizza_type)

    print(len(pizza_index))
    print(", ".join(pizza_index))
