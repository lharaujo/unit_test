# importing function from another script
from function import total

""" running tests """

# Basic operation check:
print(total([1, 2 ,3]) == 6)

# Verify that the sum works with a negative and a positive number:
print(total([1, -1]) == 0)

# Verify that the sum works with two negative numbers:
print(total([-1, -1]) == -2)

# Verify that the sum works with only one element:
print(total([1]) == 1)

# Verify that the empty list returns 0:
print(total([]) == 1)