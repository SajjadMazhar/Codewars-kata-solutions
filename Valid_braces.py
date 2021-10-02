
def validBraces(string):
    stack=[]
    opening='({['
    closing=')}]'
    for brace in string:
        if brace in opening:
            stack.append(brace)
        elif brace in closing:
            position=closing.index(brace)
            if len(stack)>0 and opening[position]==stack[len(stack)-1]:
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False

validBraces('(}')

