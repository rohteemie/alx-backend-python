#!/usr/bin/env python3
"""
  Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of all list float element"""
    list_sum: float = 0
    num: float
    for num in input_list:
        list_sum += num
    return list_sum
