# importing function from another script
from function import total


def test_total():

    """ running tests """
    assert total([1, 2, 3]) == 6

    assert total([1, -1]) == 0

    assert total([-1, -1]) == -2

    assert total([1]) == 1

    assert total([]) == 0
