def unique_characters(x):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if (x[i] == x[j]):
                return False

    return True


x = "abcde"

if (unique_characters(x)):
    print('True')
else:
    print('False')