import pytest
import merge_sorted_arrays

def test_array_1():
    result = merge_sorted_arrays.merge_sorted_arrays([1, 3, 5], [])
    assert result == [1, 3, 5]

def test_array_2():
    result = merge_sorted_arrays.merge_sorted_arrays([1, 3, 5], [2, 4, 6])
    assert result == [1, 2, 3, 4, 5, 6]

def test_array_3():
    result = merge_sorted_arrays.merge_sorted_arrays([1, 3], [2, 4, 6, 7])
    assert result == [1, 2, 3, 4, 6, 7]

def test_array_4():
    result = merge_sorted_arrays.merge_sorted_arrays([5], [2, 4, 6, 7])
    assert result == [2, 4, 5, 6, 7]

def test_array_5():
    result = merge_sorted_arrays.merge_sorted_arrays([], [2, 4, 6, 7])
    assert result == [2, 4, 6, 7]

