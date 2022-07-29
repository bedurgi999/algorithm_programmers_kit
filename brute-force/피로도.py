# 프로그래머스 고득점 kit 완전탐색 피로도 level 2
# 결과 : 정답 
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    order = [i for i in range(len(dungeons))]
    order_list = permutations(order, len(order))
    
    for o in order_list:
        a = k
        temp = 0
        for i in o:
            if a >= dungeons[i][0]:
                a -= dungeons[i][1]
                temp += 1
        if temp > answer:
            answer = temp
            
        
    
    return answer

"""
풀이
피로도 문제에서 던전의 개수가 1개 이상 8개 이하라고 명시 되어있다.
그래서 던전 개수에 대한 인덱스 0~n 까지의 번호를 permutations(순열)을 사용해 탐험할 수 있는 모든 경우의 수를 만든다.
그리고 탐험 순서가 저장된 리스트를 하나씩 불러와 던전 탐험 조건에 맞게 구현해 제일 많이 탐험된 값을 답으로 반환해준다. 
"""