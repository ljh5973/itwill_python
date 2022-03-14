def asterisk_test(a, *args):
    print(a, args)
    print(type(args))
    
asterisk_test(1,2,3,4,5) # 1(2,3,4,5)

def asterisk_test(a, *args):
    print(a, *args)
    print(type(args))

# args 앞에 * 붙이면 unpacking이 된다.
asterisk_test(1, 2,3,4,5) # 1 2 3 4 5

def asterisk_test(a, **kargs):
    print(a,kargs)
    print(type(kargs))

asterisk_test(1, b=2,c=3,d=4) # 1{'b': 2, 'c':3, 'd': 4}

a,b,c=([1,2],[3,4],[5,6])
print(a,b,c)        # [1,2] [3,4] [5,6]

data=([1,2],[3,4],[5,6])
print(*data)        # [1,2] [3,4] [5,6]

for data in zip(*([1,2],[3,4],[5,6])):
    print(data)         # (1,3,5) (2,4,6)

def asterisk_test(a,b,c,d):
    print(a,b,c,d)
    
data={'b':1, 'c':2, 'd':3}
asterisk_test(10, **data) # 10 1 2 3