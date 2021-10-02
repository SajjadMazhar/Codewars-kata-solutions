def calc_type(a, b, res):
    if res==a+b:
        return 'addition'
    elif res==a*b:
        return 'multiplication'
    elif res==a-b:
        return 'subtraction'
    elif res==a/b:
        return 'division'