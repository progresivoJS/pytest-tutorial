from tutorial.calculator import Calculator
import pytest
from unittest import mock


@pytest.fixture
def calc():
    return Calculator()


def mock_sum(a, b):
    return a + b


# @mock.patch('tutorial.calculator.Calculator.sum', return_value = 6)
@mock.patch('tutorial.calculator.Calculator.sum')
def test_sum(mock_calculator_sum, calc):
    mock_calculator_sum.return_value = 6
    assert calc.sum(23, 4) == 6


@mock.patch('tutorial.calculator.Calculator.sum')
def test_sum_with_side_effect(mock_calculator_sum, calc):
    mock_calculator_sum.side_effect = mock_sum
    assert calc.sum(2, 4) == 6
