def narcissistic( value ):
    result=0
    save=value
    exp=len(str(value))
    while value>0:
        result+=(value%10)**exp
        value//=10
    return True if result==save else False

narcissistic(153)

