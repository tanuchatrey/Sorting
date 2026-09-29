def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Choose the last element as pivot
    pivot = arr[-1]

    left = []
    right = []

    for i in arr[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


# Example
arr = [10, 7, 8, 9, 1, 5]

print("Original array:", arr)
print("Sorted array:", quick_sort(arr))
