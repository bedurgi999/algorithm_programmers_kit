# 프로그래머스 고득점 kit 깊이/너비 우선 탐색 타겟넘버 level 2
# 정답
def solution(numbers, target):
    answer = 0
    l = len(numbers)
    
    def dfs(cur, numbers, cnt, length, target):
        if cnt == length-1:
            if target == cur:
                nonlocal answer
                answer += 1
                return 1
            else:
                return 0
        
        dfs(cur + numbers[cnt+1], numbers, cnt+1, length, target)
        dfs(cur - numbers[cnt+1], numbers, cnt+1, length, target)
    
    dfs(-numbers[0], numbers, 0, l, target)
    dfs(numbers[0], numbers, 0, l, target)
    
    return answer

"""
풀이
재귀함수 사용
예시 : [1, 1, 1, 1, 1]에서 모든 경우의 수를 다 확인해서 최종적으로 target값과 같으면 answer += 1 해줌
처음에 -1, 1 로 시작
-1에서 -1+1, -1-1 
1에서 1+1, 1-1 
계속 이런식으로 한 개는  더해주고, 한 개는 빼주는 형태로 재귀함수 구성
"""