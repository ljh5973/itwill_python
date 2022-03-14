from random import random
import random
import math
import numpy as np

print("a")
# 함수 이름: make_list
# 기능 start 이상 end 미만의 정수 난수 n개를 갖는 리스트를 반환
def make_list(start, end, n):
    row=[random.randrange(start,end) for _ in  range(n)]
    return row

print(make_list(1,5,5))
num=make_list(1,5,5)

# 함수 이름 calc_sum
# 기능 : 숫자들을 저장하고 있는 리스트의 모든 원소들의 합을 반환
def calc_sum(row):
    result=0
    for i in row:
        result+=i
    return result

print(calc_sum(num))
# 함수 이름: calc_mean
# 기능: 숫자들을 저장하고 있는 리스트의 모든 원소들의 평균을 반환
def calc_mean(row):
    result=calc_sum(row)/len(row)
    
    return result

print(calc_mean(num))


# 함수 이름: calc_variance
# 기능: 숫자들을 저장하고 있는 리스트의 원소들의 분산을 반환
def calc_variance(num):
    result=np.var(num)
    return result

print(calc_variance(num))
# 함수 이름: calc_stddev
# 기능: 숫자들을 저장하고 있는 리스트의 원소들의 표준 편차를 반환

def calc_stddev(num):
    result= np.std(num)
    return result

print(calc_stddev(num))
