def DescendingSelectionSort(arr):
    for i in range(len(arr) - 1):
        x = i
        for j in range(len(arr) - 1, i, -1):
            if arr[j] > arr[x]:
                x = j
        if x != i:
            arr[i], arr[x] = arr[x], arr[i]
    return arr


test_arr = [10, 4, 7, 12, 8, 3, 1, 9]
print(DescendingSelectionSort(test_arr))
