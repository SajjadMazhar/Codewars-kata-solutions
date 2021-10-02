def toCsvText(array):
    for i in range(len(array)):
        if i > 0:
            print("\\n", end='')
        for j in array[i]:
            print(f"{j}", end=',')




toCsvText([[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 3, 7, 5]])
