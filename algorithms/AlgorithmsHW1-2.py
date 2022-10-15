
def maximum(n1, n2, n3):
    if (n1 >= n2) and (n1 >= n3):
        greatest = n1
    elif (n2 >= n1) and (n2 > n3):
        greatest = n2
    else:
        greatest = n3
    return greatest


n1 = 250
n2 = 360
n3 = 52

print('Maximum number is', maximum(n1, n2, n3))