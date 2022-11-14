def Descending_Insertion_Sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and x > arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            arr[j + 1] = x
    return arr


test_arr = [-14, 9, 4, -12, 8, 3, 1]
print(Descending_Insertion_Sort(test_arr))
