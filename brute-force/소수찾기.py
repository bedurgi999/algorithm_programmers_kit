# 프로그래머스 고득점 kit 완전탐색 소수찾기 level 2
# 결과 : 시간초과
from itertools import permutations

def Eratos(num):
    sieve = [True] * num
    
    n = int(num ** 0.5)
    
    for i in range(2, n+1):
        if sieve[i] == True:
            for j in range(i+i, num, i):
                sieve[j] = False
    
    return [i for i in range(2, num) if sieve[i] == True]

def solution(numbers):
    answer = 0
    temp = []
    
    nums = list(numbers)
    e = Eratos(int(''.join(sorted(nums, reverse=True)))+1)
    for i in range(1, len(nums) + 1):
        num_list = permutations(nums, i)
        for num in num_list:
            a = int(''.join(list(num)))
            if a in e:
                temp.append(a)
                
    answer = len(list(set(temp)))
    return answer

"""
풀이
에라토스테네스 체를 사용한 문제풀이
"""