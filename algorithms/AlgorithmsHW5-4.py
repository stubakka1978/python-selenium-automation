def Descending_Merge_Sort(arr1, beg, end):
    if end - beg > 1:
        mid = (beg + end) // 2
        Descending_Merge_Sort(arr1, beg, mid)
        Descending_Merge_Sort(arr1, mid, end)
        arr(arr1, beg, mid, end)


def arr(arr1, beg, mid, end):
    left = arr1[beg:mid]
    right = arr1[mid:end]
    k = beg
    i = 0
    j = 0
    while beg + i < mid and mid + j < end:
        if left[i] <= right[j]:
            arr1[k] = left[i]
            i = i + 1
        else:
            arr1[k] = right[j]
            j = j + 1
        k = k + 1
    if beg + i < mid:
        while k < end:
            arr1[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            arr1[k] = right[j]
            j = j + 1
            k = k + 1


test_arr = [9, 7, 3, 5, 2, 1, 0, 8]

Descending_Merge_Sort(test_arr, 0, len(test_arr))

test_arr.reverse()
print(test_arr)
