#!/usr/bin/env python3
"""
  Complex types - list of floats
"""


def sum_list(input_list: float) -> float:
    list_sum: float = 0
    num: float
    for num in input_list:
        list_sum += num
    return list_sum
