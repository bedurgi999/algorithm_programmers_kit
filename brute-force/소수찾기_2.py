# 제곱근까지의 숫자로 나누어보기
# 결과 : 정답
from itertools import permutations

def solution(numbers):
    answer = 0

    answer_list = []
    num = list(numbers)
    for i in range(1, len(num)+1):
        num_list = permutations(num, i)
        for n in num_list:
            check = True
            temp = int(''.join(list(n)))
            if temp == 0 or temp == 1:
                continue
            
            s = int(temp ** 0.5 + 1)
            
            for j in range(2, s):
                if temp % j == 0:
                    check = False
                    break
            if check:
                answer_list.append(temp)
                
    answer = len(list(set(answer_list)))
    return answer