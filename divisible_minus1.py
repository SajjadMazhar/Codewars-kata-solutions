def how_many_times(a, b):
    if a > b :a, b = b, a
    counter = 0
    while (a > 0):
        if b % a == 0:
            counter += 1
            a, b = a - 1, b - 1
        else:
            a, b = a - 1, b - 1
    return counter

print(how_many_times(3,5))