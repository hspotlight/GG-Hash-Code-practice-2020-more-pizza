from src.pizza import Pizza, PizzaCalculator, getInput
import os

test_inputs_dir = './test_inputs'
test_outputs_dir = './test_outputs'

def hanle_read_file(input_file_path):
    f = open(input_file_path, "r")
    content = f.read()
    content = content.split('\n')
    return [content[0], content[1]]

def handle_write_file(output_file_path, pizza_index):
    f = open(output_file_path, "w")
    f.write("%d\n" % len(pizza_index))
    f.write("%s\n" % " ".join(pizza_index))

for filename in os.listdir(test_inputs_dir):
    if (filename in ['e_also_big.in']):
        continue
    
    input_file_path = os.path.join(test_inputs_dir, filename)
    output_file_path = os.path.join(test_outputs_dir, filename[:-3] + ".out")

    [line1, line2] = hanle_read_file(input_file_path)

    print(filename)
    [pizza_types, target_slice] = getInput(line1, line2)
    pizza_index = PizzaCalculator.get_ordered_pizza_index(pizza_types, target_slice)
    print(pizza_index)
    handle_write_file(output_file_path, pizza_index)
