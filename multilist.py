from random import random


import random
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]



for row in matrix:
    print(row)
    
for row in matrix:
    for x in row:
        print(x,  end=' ')

print()        
matrix1=[] # 빈 리스트 1차원 리스트들을 저장하기 위한 리스트
for _ in range(3):
    row=[]  # 빈 리스트 - 3개의 난수를 저장하기 위한 리스트.
    for _ in range(3):
        row.append(random.randrange(10))
    matrix1.append(row)
print(matrix1)


matrix2=[]
for _ in range(3):
    row=[random.randrange(10) for _ in range(3)]
    matrix2.append(row)

print(matrix2)


matrix3=[[random.randrange(10)for _ in range(3)] 
         for _ in range(3)]

print(matrix3)

adds=[]
for row1,row2 in zip(matrix1, matrix2):
    temp= []
    for x, y in zip(row1, row2):
        temp.append(x+y)
    adds.append(temp)

print(adds)   


adds=[]
for row1,row2 in zip(matrix1, matrix2):
    temp=[x+y for x,y in zip(row1, row2)]
    adds.append(temp)
    
print(adds)

adds=[[x+y for x,y in zip(row1,row2)]
      for row1, row2 in zip(matrix1,matrix2)]

