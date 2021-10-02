def solution(n):
    roman=''
    numbers={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
    
    if n>=1000:
        quo=n//1000
        n=n%1000
        roman=roman+quo*'M'
    elif n>=500 and n<1000:
        quo=n//500
        n=n%500
        roman=roman+quo*'C'
    elif n>=100 and n<500:
        quo=n//100
        n=n%100
        roman=roman+quo*'L'
    print(roman)
    
solution(10)
