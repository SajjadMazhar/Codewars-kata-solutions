def dig_pow(n, p):
    sum=0
    num=n
    length=len(str(n))
    for increment in range(p+length-1, p-1, -1 ):
       if n!=0:
            dig=n%10
            sum=sum+dig**increment
            n=n//10
       else:
           break

    if sum%num==0:
        return  (sum/num)

    else:
        return -1

print(dig_pow(443,4))