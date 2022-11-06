def even_odd(arr):
    even_no = 0
    odd_no = len(arr) - 1

    while even_no < odd_no:
        if arr[even_no] % 2 == 0:
            even_no += 1
        else:
            arr[even_no], arr[odd_no] = arr[odd_no], arr[even_no]
            odd_no -= 1
    return arr


test_list = [7, 3, 5, 6, 4, 10, 3, 2]
print(even_odd(test_list))
