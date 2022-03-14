numbers=[1,-2,3,-4,5,-6]
def my_mapper(iterable, fn):
    """
     iterable의 원소를 차례로 합수 fn의 argument로 전달해서. 함수 fn의 리턴값들로 이루어진 리스트를 리턴.
     
     iterable: 리스트
     fn: argument가 1개이고 값을 반환하는 함수
     
    """
    result=[]
    for x in iterable:
        result.append(fn(x))
    return result
    # return [x for x in iterable if fn(x)]
print(my_mapper(numbers, lambda x: '짝' if x%2==0 else '홀'))

#  genders의 값이 '남성'이면 0 '여성'이면 1
genders=['남성','여성','남성','여성']
print(my_mapper(genders, lambda x: 0 if x=='남성' else 1))

def my_mapper2(iterable, fn):
    """
        iterable의 원소를 key로 하고,
        iterable의 원소를 함수 fn의 argument로 사용했을 때의 리턴 값을 value로 하는 dict를 리턴
        
        iterable: 리스트
        fn: argument가 1개이고 값을 반환하는 함수.
    """
    result={}
    for x in iterable:
        result[x]=fn(x)
    return result
#   return {x:fn(x) for x in iterable}
#  numbers의 값을 키로하고 짝수/홀수인 지를 value로 하는 dict
print(my_mapper2(numbers,lambda x: '짝' if x%2==0 else '홀' ))

# languages의 원소를 키로 하고 , 그 원소(문자열)의 길이를 value로 하는  dict
languages={'Java',"HTML","JavaScript","Python"}
print(my_mapper2(languages, lambda x: len(x)))


# 