import math


def lowest_elements(x):
    list_size = len(x)
    if list_size < 2:
        print("Invalid Input")
        return

    first = second = math.inf
    for i in range(0, list_size):

        if x[i] < first:
            second = first
            first = x[i]

        elif x[i] < second and x[i] != first:
            second = x[i]

    if second == math.inf:
        print("No second smallest element")
    else:
        print('The smallest element is', first, 'and',
              ' second smallest element is', second)


x = [198, 3, 4, 9, 10, 9, 2]
print(lowest_elements(x))
