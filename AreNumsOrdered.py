def arr(n):
    if n==0:
        return []
    else:
        return list(range(n))
try:
    arr()
except Exception as e:
    print(e)