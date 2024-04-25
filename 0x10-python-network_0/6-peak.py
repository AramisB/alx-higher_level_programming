#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return (list_of_integers)[0]

    mid_index = int(len(list_of_integers)/2)

    if mid_index != len(list_of_integers) - 1:
        if list_of_integers[mid_index - 1] < list_of_integers[mid_index] and\
              list_of_integers[mid_index + 1] < list_of_integers[mid_index]:
            return (list_of_integers[mid_index])

    else:
        if list_of_integers[mid_index - 1] < list_of_integers[mid_index]:
            return (list_of_integers[mid_index])
        else:
            return (list_of_integers[mid_index - 1])

    if list_of_integers[mid_index - 1] > list_of_integers[mid_index]:
        list_a = list_of_integers[:mid_index]

    else:
        list_a = list_of_integers[mid_index + 1:]
    return find_peak(list_a)
