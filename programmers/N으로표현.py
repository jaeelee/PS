from itertools import product

"""
    DP를 이용하는 문제
    숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성

    DP[1] => N을 1번 사용한 표현방법
    DP[2] => N을 2번 사용한 표현방법
    ...
    과 같은 식으로 구해 나가면 된다.

    주의 > 
    ex) DP[4]일 경우 아래의 경우의 수 모두 고려해야한다. 
        1. DP[1] (사칙연산) DP[3]
        2. DP[2] (사칙연산) DP[2]
        3. DP[3] (사칙연산) DP[1]
"""

def solution(N, number):
    dp = [[0]] + [ [ int(str(N) * i) ] for i in range(1, 9) ]

    if number == N:
        return (1)

    for i in range(2, 9):
        for j in range(1, i):
            dp[i] += [ x + y for x, y in set(product(dp[j], dp[i - j])) ]
            dp[i] += [ x * y for x, y in set(product(dp[j], dp[i - j])) ]
            dp[i] += [ x - y for x, y in list(product(dp[j], dp[i - j])) ]
            dp[i] += [ x // y for x, y in list(product(dp[j], dp[i - j])) ]
        dp[i] = [i for i in list(set(dp[i])) if i != 0]
        if number in dp[i]:
            return (i)

    return -1