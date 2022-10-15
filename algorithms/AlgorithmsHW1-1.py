
def sum_of_digits(n):
    result = 0
    for i in range(1, n + 1):
        result = result + i
    return result


n = 5
print('Sum of digits in numbers from 1 to', n, 'is', sum_of_digits(n))