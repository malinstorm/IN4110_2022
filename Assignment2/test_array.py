"""
Tests for our array class
"""
#import pytest
from array_class import Array
#from implementation_testing import Array
import math
# 1D tests (Task 4)


def test_str_1d():
    array1 = Array(shape1, 6,3,49,1)

def test_add_1d():
    array1 = Array(shape1, 4,3,9,1)
    array2 = Array(shape2, 2,3,0,9)

    array3 = Array((4,), [[6,6,9,10]]) #validation array
    assert array1 + array2 == array3
    assert array2 + array1 == array3

    array4 = Array(shape1, 0.7,5.6,2.1,1.7)
    array5 = Array(shape2, 3.7,1.6,2.9,-1.7)

    array6 = Array((4,), [[4.4,7.2,5,0]]) #validation array
    assert array4 + array5 == array6
    assert array5 + array4 == array6

    # tester _skalar_ og __radd__
    i = 10
    array7 = Array((4,), [[14,13,19,11]])
    assert array7 == array1 + i
    assert array7 == i + array1


def test_sub_1d():
    array1 = Array(shape1, 4,3,9,1)
    array2 = Array(shape2, 2,3,0,9)

    array3 = Array((4,), [[2,0,9,-8]]) #validation array
    assert array1 + array2 == array3
    array4 = Array((4,), [[-2,0,-9,8]]) #validation array
    assert array2 + array1 == array4

    array6 = Array(shape1, 0.7,5.6,2.1,1.7)
    array7 = Array(shape2, 3.7,1.6,2.9,-1.7)

    array5 = Array((4,), [[-3.0,3.99,-0.79, 3.4]]) #validation array
    assert array6 - array7 == array5
    array8 = Array((4,), [[3.0,-3.99,0.79,-3.4]]) #validation array
    assert array7 - array6 == array8

    #tester _skalar_ og __rsub__
    i = 10
    array9 = Array((4,),[[-6,-7,-1,-9]])
    assert array9 == array1 - i
    array10 = Array((4,), [[6,7,1,9]])
    assert array10 == i - array1

def test_mul_1d():
    # testing negative/positive int
    array1 = Array(shape1, 4,3,9,1)
    array2 = Array(shape2, 2,3,0,-9)

    array3 = Array((4,), [[8,9,0,-9]]) #validation array
    assert array1 * array2 == array3
    assert array2 * array1 == array3

    # testing negative/positive float
    array4 = Array(shape1, 0.7,5.6,2.1,1.7)
    array5 = Array(shape1, 3.7,1.6,2.9,-1.7)

    array6 = Array((4,),[[2.59,8.959,6.09,-2.889]]) #validation array
    assert array4 * array5 == array6
    assert array5 * array4 == array6

    # tester _skalar_ og __rmul__
    i = 10
    array7 = Array((4,), [[40,30,90,10]])
    assert array7 == array1 * 10
    assert array7 == 10 * array1

def test_eq_1d():
    shape = 4
    array1 = Array(shape, (1,2,3,4))
    array2 = Array(shape, (7,8,9,19))
    #Array.__eq__(array1,array2)

    assert array1 == array2

    array3 = Array(shape, 4.5,3.4,9.2,1.6)
    array4 = Array(shape, 6.1,3.3,0.6,9.0)
    assert array3 == array4

def test_same_1d():
    # tester med int
    array1 = Array((3,), 4,3,9)
    array2 = Array((3,), 2,3,0)
    array3 = Array((3),[True,True,True]) #validation array
    array4 = Array.is_equal(array1,array2)

    for key in range(len(array3)):
        assert (array3[key]) == (array4[key])

    #tester med både int mot float
    array5 = Array((3,), 4,3,9)
    array6 = Array((3,), 2.1,3.4,0.6)
    array7 = Array((3),[False,False,False]) #validation array
    array8 = Array.is_equal(array5,array6)

    for key in range(len(array7)):
        assert (array7[key]) == (array8[key])

    # tester at det fanges opp at datatypene er blandet
    array9 = Array((3,), 4.8,3,9)
    array10 = Array((3,), 2.1,3.4,0.6)
    array11 = Array((3),[True,False,False]) #validation array
    array12 = Array.is_equal(array9,array10)

    for key in range(len(array7)):
        assert (array11[key]) == (array12[key])

def test_smallest_1d(): #tester med både int og float
    array1 = Array(shape1, 4,3,9,1) #validation array
    min = Array.min_element(array1)
    assert min == 1

    array2 = Array(shape1, 4.3,3.2,-0.9,1) #validation array
    min = Array.min_element(array2)
    assert min == -0.9

def test_mean_1d(): #tester med både int og float
    array1 = Array(shape1, 4,3,9,1) #validation array
    mean = Array.mean_element(array1)
    assert mean == 4.25

    array2 = Array(shape1, 4.3,3.2,-0.9,1) #validation array
    mean = Array.mean_element(array2)
    assert mean == 1.9






# 2D tests (Task 6)


def test_add_2d():
    pass


def test_mult_2d():
    pass


def test_same_2d():
    pass

def test_mean_2d():
    pass


#if __name__ == "__main__":
#    """
#    Note: Write "pytest" in terminal in the same folder as this file is in to run all tests
#    (or run them manually by running this file).
#    Make sure to have pytest installed (pip install pytest, or install anaconda).
#    """

    # Task 4: 1d tests
#    test_str_1d()
#    test_add_1d()
#    test_sub_1d()
#    test_mul_1d()
#    test_eq_1d()
#    test_mean_1d()
#    test_same_1d()
#    test_smallest_1d()

    # Task 6: 2d tests
#    test_add_2d()
#    test_mult_2d()
#    test_same_2d()
#    test_mean_2d()
shape1 = (4,)
shape2 = (4,)
test_str_1d()
test_mean_1d()
test_smallest_1d()
test_eq_1d()
test_same_1d()
test_add_1d()
test_sub_1d()
test_mul_1d()
