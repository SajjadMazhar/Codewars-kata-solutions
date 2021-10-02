#Original Matrix
x = [[1,2],[3,4],[5,6]]
result = map(list, zip(*x))
for r in result:
   print(r)
exit()
#Original Matrix
x = [[1,2],[3,4],[5,6]]
result = [[0, 0, 0], [0, 0, 0]]
# Iterate through rows
for i in range(len(x)):
   #Iterate through columns
   for j in range(len(x[0])):
      result[j][i] = x[i][j]
for r in result:
    print(r)