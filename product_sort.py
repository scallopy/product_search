from random import randrange


my_list = [
    ['Some', 'Something', 121],
    ['This', 'Thisthing', 12],
    ['Mine', 'Description', 23],
    ['Asterisks', 'Description', 1222],
    ['Nolan', 'Description', 34]
]

# print(my_list)


def quicksort(arr, start, end):
    count = 0
    if start >= end:
        return arr
    pivot_idx = randrange(start, end)
    pivot_element = arr[pivot_idx]

    count += 1
    # print("Pivot element: ", pivot_element)
    # print("Iterations: ", count)
    arr[pivot_idx], arr[end] = arr[end], arr[pivot_idx]
    less_than_pointer = start
    for idx in range(start, end):
        if arr[idx][0][0] < pivot_element[0][0]:
            arr[idx], arr[less_than_pointer] = arr[less_than_pointer], arr[idx]
            less_than_pointer += 1

    arr[less_than_pointer], arr[end] = arr[end], arr[less_than_pointer]
    quicksort(arr, start, less_than_pointer - 1)
    quicksort(arr, less_than_pointer + 1, end)

    start += 1
    return quicksort(arr, start, end)


# print(quicksort(my_list, 0, (len(my_list) - 1)))
