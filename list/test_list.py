from re import I
from list import merge_lists, merge_lists_inplace, find_product

def test_merge_lists():
    list1 = [1,3,4,5]
    list2 = [2,6,7,8]
    assert merge_lists(list1, list2) == [1,2,3,4,5,6,7,8]
    assert merge_lists_inplace(list1, list2) == [1,2,3,4,5,6,7,8]

def test_find_product():
    assert find_product([1,2,3,4], ) == [24,12,8,6]