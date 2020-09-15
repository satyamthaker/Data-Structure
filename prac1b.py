m1 = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]


m2 = [[10,11,12,13],
    [14,15,16,17],
    [18,19,20,21]]

res = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]


for i in range(len(m1)):
  
   for j in range(len(m2[0])):
       
       for k in range(len(m2)):
           res[i][j] += m1[i][k] * m2[k][j]

for n in res:
   print(n)
