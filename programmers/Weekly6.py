"""
boxer의 몸무게와 전적이 주어졌을 때
    1. 승률이 높은 순서
    2. 자신보다 더 무거운 복서를 이긴 횟수 가 큰 순서
    3. 몸무게가 많은 순서
로 정렬하기

args:
    weights: boxer의 몸무게
    head2head: boxer의 승률. W는 win, L은 Lose, N은 none(경기한 적 없음)
"""

def solution(weights, head2head):
    answer = []
    length = len(weights)
    info = [[i, weights[i - 1], 0, 0]  for i in range(1, length + 1)]
        
    for i in range(length):
        if (length > head2head[i].count('N')):
            info[i][2] = head2head[i].count('W') / (length - head2head[i].count('N'))
        info[i][3] = len([j for j in range(length) 
                          if (head2head[i][j] == 'W' and weights[i] < weights[j])])
        
    info = sorted( info, key = lambda x : (-x[2], -x[3], -x[1]) )
    answer = [i[0] for i in info]
                
    return answer