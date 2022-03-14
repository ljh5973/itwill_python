u=[2,2]
v=[2,3]
z=[3,5]
result=[sum(t) for t in zip(u,v,z)]
print(result)


#Scalar-Vector product

u=[1,2,3]
v=[4,4,4]
alpha =2

result= [alpha*sum(t) for t in zip(u,v)]
print(result)

matrix_a=[[3,6],[4,5]]
matrix_b=[[5,8],[6,7]]

result=[[sum(r) for r in zip(t,v)] for t,v in zip(matrix_a, matrix_b)]
print(result)


# Matrix Transpose
matrix_a=[[1,2,3],[4,5,6]]
result=[[e for e in t] for t in zip(*matrix_a)]
print(result)


# Matrix Product
# *로 dict를 풀어준 다음 column을 3개의 row로 바꿔서 곱해준다.
matrix_a=[[1,1,2],[2,1,1]]
matirx_b=[[1,1],[2,1],[1,3]]

result=[[sum(a*b for a, b in zip(row_a, column_b))  for column_b in zip(*matrix_b)] for row_a in matrix_a]

print(result)

# 재귀 함수(recursive function)

# 함수 내부에서 자기 자신을 다시 호출하는 함수

def factorial(n):
    """
    0! = 1(정의)
    1! = 1  = 0! x 1
    2! = 1 x 2 = 2  = 1! x 2
    3! = 1 x 2 x 3 =6  = 2! x 3
    ...
    
    n! = 1 x 2 x ... x (n-1) x n = (n-1)! x n ,  n >= 1
    """
    result= None
    if n==0:
        result=1
    elif n > 0 :
        result=factorial(n-1) * n
    return result

for n in range(6):
    print(factorial(n))

print(factorial(5))