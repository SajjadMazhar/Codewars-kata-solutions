def create_array_of_tiers(n):
    num=[]
    while n>0:
        num.append(n)
        n=n//10
    num.sort()
    num=list(map(str, num))

    return num
create_array_of_tiers(2017)
