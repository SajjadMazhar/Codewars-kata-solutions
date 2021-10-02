def tribonacci(signature, n):
    a=signature[0]
    b=signature[1]
    c=signature[2]
    new_series.append(a)
    new_series.append(b)
    new_series.append(c)

    for i in range(3,n):
        d=a+b+c
        new_series.append(d)
        a=b
        b=c
        c=d
    print(new_series)


signature=[1,1,1]
n=10

new_series = []

tribonacci(signature,n)

