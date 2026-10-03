"""
Tests for our homemade Array class
"""

from array_class import Array
import math


shape1 = (4,)
shape2 = (4,)


def assert_array_close(array1, array2):
    # tester arrays med float uten at små avrundingsfeil ødelegger testen

    assert array1.shape == array2.shape
    assert len(array1) == len(array2)

    for key in range(len(array1)):
        assert math.isclose(
            array1[key],
            array2[key],
            rel_tol=1e-9,
            abs_tol=1e-9
        )


# 1D tests (Task 4)


def test_str_1d():

    array1 = Array(shape1, 6, 3, 49, 1)

    assert str(array1) == "[6, 3, 49, 1]"


def test_add_1d():

    # testing ints
    array1 = Array(shape1, 4, 3, 9, 1)
    array2 = Array(shape2, 2, 3, 0, 9)

    array3 = Array((4,), 6, 6, 9, 10)  # validation array

    assert array1 + array2 == array3
    assert array2 + array1 == array3

    # testing floats
    array4 = Array(shape1, 0.7, 5.6, 2.1, 1.7)
    array5 = Array(shape2, 3.7, 1.6, 2.9, -1.7)

    array6 = Array((4,), 4.4, 7.2, 5.0, 0.0)  # validation array

    assert_array_close(array4 + array5, array6)
    assert_array_close(array5 + array4, array6)

    # tester skalar og __radd__
    i = 10

    array7 = Array((4,), 14, 13, 19, 11)

    assert array1 + i == array7
    assert i + array1 == array7


def test_sub_1d():

    # testing ints
    array1 = Array(shape1, 4, 3, 9, 1)
    array2 = Array(shape2, 2, 3, 0, 9)

    array3 = Array((4,), 2, 0, 9, -8)  # validation array
    array4 = Array((4,), -2, 0, -9, 8)  # validation array

    assert array1 - array2 == array3
    assert array2 - array1 == array4

    # testing floats
    array5 = Array(shape1, 0.7, 5.6, 2.1, 1.7)
    array6 = Array(shape2, 3.7, 1.6, 2.9, -1.7)

    array7 = Array((4,), -3.0, 4.0, -0.8, 3.4)
    array8 = Array((4,), 3.0, -4.0, 0.8, -3.4)

    assert_array_close(array5 - array6, array7)
    assert_array_close(array6 - array5, array8)

    # tester skalar og __rsub__
    i = 10

    array9 = Array((4,), -6, -7, -1, -9)
    array10 = Array((4,), 6, 7, 1, 9)

    assert array1 - i == array9
    assert i - array1 == array10


def test_mul_1d():

    # testing negative/positive int
    array1 = Array(shape1, 4, 3, 9, 1)
    array2 = Array(shape2, 2, 3, 0, -9)

    array3 = Array((4,), 8, 9, 0, -9)  # validation array

    assert array1 * array2 == array3
    assert array2 * array1 == array3

    # testing negative/positive float
    array4 = Array(shape1, 0.7, 5.6, 2.1, 1.7)
    array5 = Array(shape2, 3.7, 1.6, 2.9, -1.7)

    array6 = Array((4,), 2.59, 8.96, 6.09, -2.89)

    assert_array_close(array4 * array5, array6)
    assert_array_close(array5 * array4, array6)

    # tester skalar og __rmul__
    i = 10

    array7 = Array((4,), 40, 30, 90, 10)

    assert array1 * i == array7
    assert i * array1 == array7


def test_eq_1d():

    array1 = Array((4,), 1, 2, 3, 4)
    array2 = Array((4,), 1, 2, 3, 4)
    array3 = Array((4,), 1, 2, 3, 5)

    assert array1 == array2
    assert not (array1 == array3)


def test_same_1d():

    array1 = Array((3,), 4, 3, 9)
    array2 = Array((3,), 2, 3, 0)

    array3 = Array((3,), False, True, False)  # validation array
    array4 = Array.is_equal(array1, array2)

    assert array3 == array4

    # tester med int mot float
    array5 = Array((3,), 4, 3, 9)
    array6 = Array((3,), 4.0, 3.4, 9.0)

    array7 = Array((3,), True, False, True)  # validation array
    array8 = Array.is_equal(array5, array6)

    assert array7 == array8


def test_smallest_1d():

    # tester med int
    array1 = Array(shape1, 4, 3, 9, 1)

    minimum = Array.min_element(array1)

    assert minimum == 1

    # tester med float
    array2 = Array(shape1, 4.3, 3.2, -0.9, 1)

    minimum = Array.min_element(array2)

    assert minimum == -0.9


def test_mean_1d():

    # tester med int
    array1 = Array(shape1, 4, 3, 9, 1)

    mean = Array.mean_element(array1)

    assert mean == 4.25

    # tester med int og float
    array2 = Array(shape1, 4.3, 3.2, -0.9, 1)

    mean = Array.mean_element(array2)

    assert math.isclose(mean, 1.9)


# 2D tests (Task 6)


def test_add_2d():

    array1 = Array((2, 2), [[1, 2], [3, 4]])
    array2 = Array((2, 2), [[5, 6], [7, 8]])

    validation = Array((2, 2), [[6, 8], [10, 12]])

    assert array1 + array2 == validation


def test_mult_2d():

    array1 = Array((2, 2), [[1, 2], [3, 4]])
    array2 = Array((2, 2), [[5, 6], [7, 8]])

    validation = Array((2, 2), [[5, 12], [21, 32]])

    assert array1 * array2 == validation


def test_same_2d():

    array1 = Array((2, 2), [[1, 2], [3, 4]])
    array2 = Array((2, 2), [[1, 5], [3, 8]])

    validation = Array((2, 2), [[True, False], [True, False]])

    assert Array.is_equal(array1, array2) == validation


def test_mean_2d():

    array1 = Array((2, 2), [[1, 2], [3, 4]])

    assert Array.mean_element(array1) == 2.5


if __name__ == "__main__":

    # Task 4: 1D tests
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_same_1d()
    test_smallest_1d()
    test_mean_1d()

    # Task 6: 2D tests
    test_add_2d()
    test_mult_2d()
    test_same_2d()
    test_mean_2d()

    print("All tests passed")