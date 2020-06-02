# encoding': UTF-8


# Algo02:

def selection_sort(arr):
    new_arr = []

    for i in range(len(arr)):
        smallest_item = find_smallest(arr)
        new_arr.append(arr.pop(smallest_item))

    return new_arr


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


print('result: ' + str(selection_sort([5, 3, 6, 2, 10])))
