from tutorial import math_func
import sys
import pytest


@pytest.mark.skipif(sys.version_info < (3, 3), \
    reason="I don't want to test this.")
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7
    print("hello")


@pytest.mark.number
def test_product():
    assert math_func.product(3, 7) == 21
    assert math_func.product(3, 0) == 0
    assert math_func.product(5) == 10


@pytest.mark.string
def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldlo' not in result


@pytest.mark.string
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result


def test_add_float():
    result = math_func.add(10.5, 25.5)
    assert result == 36


@pytest.mark.custom
@pytest.mark.parametrize('x, y, result',
                        [
                            (7, 3, 10),
                            ('Hello', ' World', 'Hello World'),
                            (10.5, 25.5, 36),
                        ]
                        )
def test_all_add(x, y, result):
    assert math_func.add(x, y) == result
