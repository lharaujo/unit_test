# importing function from another script
from function import total
import pytest


def test_total():

    """ running tests """
    assert total([1, 2, 3]) == 6

    assert total([1, -1]) == 0

    assert total([-1, -1]) == -2

    assert total([1]) == 1

    assert total([]) == 0


def test_total_raises_exception_on_non_list_arguments():
    with pytest.raises(TypeError):
        total(1)
