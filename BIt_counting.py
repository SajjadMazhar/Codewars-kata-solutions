def count_bit(n):
    bits=[]
    bitcount=0
    while n>0:
        rem=n%2
        if rem==0:
            bits.append('0')
            n=n//2
        else:
            bits.append('1')
            n=n//2
    bits.reverse()
    for bit in bits:
        if bit == '1':
            bitcount+=1
    return bitcount

print(count_bit(23))

