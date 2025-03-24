"""
Write a script sum_types.py that sums three elements and shows their sum as an int in the VSCode terminal. The objects to use are: 0.245, "87.0" and 104.

The result should display 191.
"""

def sum_types(e1, e2, e3):
    el1, el2, el3 = int(e1), int(float(e2)), int(e3)
    return el1 + el2 + el3

print(sum_types(0.245, "87.0", 104))