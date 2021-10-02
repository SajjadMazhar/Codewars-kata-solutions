def sum_of_minimums(numbers):
    lst=[]
    for i in numbers:
        lst.append(min(i))
    return sum(lst)
print(sum_of_minimums([ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]))
