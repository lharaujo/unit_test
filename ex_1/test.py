# importing function from another script
from function import total


def test_total():

    """ running tests """
    a = total([1, 2, 3]) == 6
    b = total([1, -1]) == 0
    c = total([-1, -1]) == -2
    d = total([1]) == 1
    e = total([]) == 0
    return (a, b, c, d, e)


print(test_total())
