import random

numbers1=[random.randrange(0,10) for _ in range(10)]
numbers2=[random.randrange(0,10) for _ in range(10)]

adds=[numbers1[i]+numbers2[i] for i in range(10)]
multi=[numbers1[i]*numbers2[i] for i in range(10)]

add=[x+y for x, y in zip(numbers1, numbers2)]
multiplications=[x*y for x,y in zip(numbers1, numbers2)]
print(add)
print("add")
print(sum(multiplications))

total=0
for x in multiplications:
    total+=x

print(total)