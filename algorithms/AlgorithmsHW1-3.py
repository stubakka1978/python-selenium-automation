def count_even_odd(n):
    even_count = 0
    odd_count = 0
    while n > 0:
        i = n % 10
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        n = int(n / 10)
    print('Even count: ', even_count)
    print('Odd count: ', odd_count)
    if even_count % 2 == 0 and odd_count % 2 != 0:
        return ""


n = 6398758965489
print(count_even_odd(n))
