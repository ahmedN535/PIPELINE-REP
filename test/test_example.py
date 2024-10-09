# Your testing code 
from src.my_math import *

def test_add():
    result = add_numbers(1,2)
    assert result == 3
def test_sub():
    result2 = subtract_numbers(1,2)
    assert result2 == 1
def test_mult():
    result3 = multiply_numbers(2,2)
    assert result3 == 4
