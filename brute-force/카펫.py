# 프로그래머스 고득점 kit 완전탐색 카펫 level 2
# 결과 : 정답 
def solution(brown, yellow):
    answer = []
    
    if yellow == 1:
        return [3, 3]
    
    for i in range(1, yellow // 2 + 1):
        if yellow % i != 0:
            continue
        row = i + 2
        col = yellow // i + 2
        if row * col - yellow == brown:
            answer.append(max(row, col))
            answer.append(min(row, col))
            break
    return answer

"""
풀이
전체 카펫 가로 길이 = yellow 가로 길이 + 2
전체 카펫 세로 길이 = yellow 세로 길이 + 2

우선 yellow 가로, 세로 길이를 찾아야 한다.
1 ~ yellow 까지 값으로 yellow를 나눠서 직사각형, 정사각형이 나올 수 있는 가로, 세로 길이를 찾는다.
여기서 1 ~ yellow까지 모두 확인할 필요 없이 yellow // 2 + 1 까지만 하면된다.
(이유 : [3, 8] == [8, 3]의 결과는 같기 때문이고 마지막에 큰 값을 가로로 작은 값을 세로로 하면된다.)

계산된 yellow의 가로, 세로 길이에 각각 +2 한 후 두 길이를 곱해주면 전체 카펫 크기가 되며, 여기에 -yellow를 해주면 brown의 개수가 될 수 있다.
그래서 row * col - yellow == brown 이 조건에 맞는 전체 카펫 가로, 세로 즉 yellow 가로 + 2, yellow 세로 + 2 해준 값을 큰 값부터 넣어 반환한다.
"""