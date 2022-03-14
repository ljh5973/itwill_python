import math

# for loop + zip
alist=['a1','a2','a3']
blist=['b1','b2','b3']

for a,b in zip(alist,blist):
    print(a,b)
    
# list comprehension + zip
a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)


# enumerate + zip
print([sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))])