#!/usr/bin/python
def only_diff_elements(set_1, set_2):
    diff = set_1.symmetric_difference(set_2)
    return diff
