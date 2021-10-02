def solve(x,y):#incomplete kata code
    n = 6
    for n in range(0, n):
        for m in range(0, 3):
            prime = 2 ** m * 3 ** n + 1
            print(prime)

solve(0,15)