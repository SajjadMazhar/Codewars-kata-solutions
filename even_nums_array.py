def even_numbers(arr,n):
    new_ar=[]
    arr.reverse()
    i=0
    while i<len(arr):
        if arr[i]%2 == 0:
            if len(new_ar)<n:
                new_ar.append(arr[i])
        i+=1
    new_ar.reverse()
    print(new_ar)


even_numbers([6, -25, 3, 7, 5, 5, 7, -3, 23], 1)
        