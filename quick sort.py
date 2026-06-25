def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


my_list = [4,54,32,312,4,5,6,43,2,22,3334,3, 6, 8, 10, 1, 2,-1,-11,-345,-3,0, 1]
sorted_list = quick_sort(my_list)
print(sorted_list)

