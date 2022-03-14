from functools import reduce
f= lambda x, y : x+ y
print (f(1,4))

f= lambda x, y : x**y

print(f(2,2))



# map = map(function_name, list_data)
ex=[1,2,3,4,5]
f=lambda x: x **2
print(list(map(f,ex)))

f= lambda x, y: x+y
# python 3 에서는 list를 반드시 붙여야함.
print(list(map(f,ex,ex)))

print(list(map(lambda x: x**2 if x%2==0 else x, ex)))

print([value **2 for value in ex])

print(reduce(lambda x,y:x+y, [1,2,3,4,5])) #15 # x = 1, y= 2 == 3 > x = 3 y = 3 == 6 > x = 6 y = 4 == 10 > x = 10 y = 5 == 15


def factorial(n):
    return reduce(lambda x,y : x*y, range(1, n+1))
print(factorial(5))