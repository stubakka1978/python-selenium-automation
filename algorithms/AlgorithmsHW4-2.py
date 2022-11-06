def plus_one(arr):
    x = len(arr) - 1

    while x >= 0 and arr[x] == 9:
        arr[x] = 0
        x -= 1

    if x < 0:

        arr.insert(0, 1)

    else:
        arr[x] += 1


test_list = [1, 2, 9]

plus_one(test_list)

for i in test_list:
    print(i, end=' ')
