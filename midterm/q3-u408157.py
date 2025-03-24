"""

Question 3

B.S. wants to order food. He wrote his rather sizeable order in order.txt with a clarification of the order after the name, and the estimated price for every item at the end. For example:

#9 two                 20
#9 large               10
#6 extra-dip           10
#7 -                    5
#45 two,1-with-cheese  25

Parameters: Write a function total_charge which as input takes one argument:
filename : a str, pointing to a file name and path (e.g., ./dir/file.txt).

Return: an int with the total amount B.S. will be charged.

Note: to test this function, create the file by copy-pasting the example contents above. Do not mess with the spaces.

Example: so,
total_charge("./cluck/order.txt")

should return:
70
"""

import os
from os.path import exists

def check_if_path_exists(file_name):
    if exists(file_name):
        return True
    else:
        return False

def total_charge(filename):
    """
    Returns the sum of the last item in a list. 

    Assumptions:
      The last item is a numeric value.
      The file exists in the same folder as this file.

    Args:
        The filename of the list.
    
    """
    cwd = os.getcwd() + "\\" + filename
    total = 0

    if check_if_path_exists(cwd) == True:
        
        with open(cwd) as order:
            in_buffer = order.readlines()
            for line in in_buffer:
                total += int(float(line.strip().split(" ")[-1]))


    return total

print(total_charge("order.txt"))

total_charge("order.txt")