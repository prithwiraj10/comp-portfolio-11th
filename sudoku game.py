# Importing the required libraries
import random

# Function to generate a Sudoku puzzle
def generate_sudoku(size):
    # Creating an empty dictionary to store the Sudoku puzzle
    my_dict = {}
    n = 0
    while len(my_dict) < 9:
        n += 1
        x = range(1, size+1)
        test_list = random.sample(x, len(x))
        is_good = True
        for dict_id, saved_list in my_dict.items():
            if is_good == False:
                break
            for v in saved_list:
                if test_list[saved_list.index(v)] == v:
                    is_good = False
                    break
        if is_good == True:
            my_dict[len(my_dict)] = test_list
    return my_dict, n

# Calling the function to generate a Sudoku puzzle
return_dict, total_tries = generate_sudoku(9)

# Printing the generated Sudoku puzzle
for n, v in return_dict.items():
    print(n, v)
print('in', total_tries, 'tries')
