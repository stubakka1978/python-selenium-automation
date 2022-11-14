def Descending_Bubble_Sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
    return arr


test_array = [4, 8, 2, 5, 9, 1, 7]
print(Descending_Bubble_Sort(test_array))
