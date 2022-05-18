from InsertionSort import *
import pytest

# Test Sample Array 
def test_Sample():
    arr =  [8,4,23,42,16,15]
    expected = [4, 8, 15, 16, 23, 42]
    actual = insertionSort(arr)
    assert expected == actual


# Reverse-sorted: 
def test_Reverse_sorted():
    arr =  [20,18,12,8,5,-2]
    expected = [-2, 5, 8, 12, 18, 20]
    actual = insertionSort(arr)
    assert expected == actual

# Few uniques: 
def test_Few_uniques():
    arr =  [5,12,7,5,5,7]
    expected = [5, 5, 5, 7, 7, 12]
    actual = insertionSort(arr)
    assert expected == actual

# Nearly-sorted: 
def test_Nearly_sorted():
    arr =  [2,3,5,7,13,11]
    expected = [2, 3, 5, 7, 11, 13]
    actual = insertionSort(arr)
    assert expected == actual



#Invalid Input
def test_Invalid_Input():
    arr = ["Ali","Ahmed",15,10]
    with pytest.raises(Exception):
        insertionSort(arr)
