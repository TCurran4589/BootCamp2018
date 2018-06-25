import pandas as pd
import numpy as np
import pytest
from math import sqrt

#Corrected smallest_factor:
'''
Answer:

raising n to the .5 power in the case where n = 9 causes incorrect result

better to use the math.sqrt() function

need to add 1 to range() bounds in order to include the square root of n

'''
def corrected_smallest_factor(n):
    '''
    Return the smallest prime factor of the positive integer n
    '''
    if n == 1:
        return(1)
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return(i)
    return(n)

def test_corrected_smallest_factor():
    assert corrected_smallest_factor(1) == 1
    assert  corrected_smallest_factor(9) == 3
    assert corrected_smallest_factor(11) == 11


################################################################################
# Question #2
################################################################################

def month_length(month, leap_year = False):
    '''

    Return the number of days in the given month

    '''

    if month in {"September","April","June","November"}:
        return(30)
    elif month in {"January","March","May","July","August","October","December"}:
        return(31)

    if month == "February":
        if not leap_year:
            return(28)
        else:
            return(29)
    else:
        return(None)

def test_month_length():
    assert month_length("September", leap_year = False) == 30, "September has 30 Days"
    assert month_length("March", leap_year = False) == 31, "March has 31 Days"
    assert month_length("February", leap_year = True) == 29, "29 Days in February on Leap Year"
    assert month_length("February", leap_year = False) == 28, "28 Days in February on Leap Year"
    assert month_length("Octoberfest", leap_year = True) is None
################################################################################
# Question #3
################################################################################

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("second input cannot be zero")

    return(a/b)


def test_divide():
    assert divide(4,2) == 2, "integer division"
    assert divide(5,4) == 1.25, "float division"
    with pytest.raises(ZeroDivisionError) as excinfo:
        divide(4,0)
    assert excinfo.value.args[0] == "second input cannot be zero"



def operate(a, b, oper):
    "Apply an arithmetic operation to a and b"
    available_operations = ('+', '/', '-', '*')


    if type(oper) is not str:
        raise TypeError("oper must be string")
    elif oper == "+":
        return(a + b)
    elif oper == "-":
        return(a-b)
    elif oper == "*":
        return(a * b)
    elif oper == "/":
        if b == 0:
            raise ZeroDivisionError("Division by Zero Undefined")
        return(a / b)
    elif oper not in available_operations:
        raise ValueError("oper must be one of '+', '/', '-', or '*'")


def test_operate():
    assert operate(2,2,"+") == 4
    assert operate(4,2,"-") == 2
    assert operate(2,3,"*") == 6
    assert operate(6,3,"/") == 2


    with pytest.raises(TypeError) as operType:
        operate(4,0, 2)

    assert operType.value.args[0] == "oper must be string"

    with pytest.raises(ValueError) as OperValError:
        operate(4,0, "t")

    assert OperValError.value.args[0] == "oper must be one of '+', '/', '-', or '*'"

    with pytest.raises(ZeroDivisionError) as zerodiv:
        operate(4,0, "/")

    assert zerodiv.value.args[0] == "Division by Zero Undefined"


import importlib.util
spec = importlib.util.spec_from_file_location("spec.py","/Users/thomascurran/Documents/GitRepos/MacroBootcamp2018/Foundations of Applied Mathematics/PythonEssentials-Student-Materials/UnitTesting/specs.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
foo.Fraction(2,3)
