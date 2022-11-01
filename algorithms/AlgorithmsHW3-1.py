import statistics


def below_a_m(x):

    avg = statistics.mean(x)
    for i in x:
        if i < avg:
            print(i, end=',')


x = [1, 3, 5, 6, 4, 10, 2, 3]
print(below_a_m(x))








