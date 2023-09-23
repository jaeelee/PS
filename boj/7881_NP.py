# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    7881.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/16 22:08:24 by jaeelee           #+#    #+#              #
#    Updated: 2022/03/16 23:08:37 by jaeelee          ###   ########seoul.kr   #
#                                                                              #
# **************************************************************************** #


def prime_list(n):
    # 에라토스테네스의 체 초기화(n개의 요소에 True 설정 = 소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:            # i가 소수인 경우
            for j in range(i + i, n , i): # i 이후 i의 배수들을 False로 판정
                sieve[j] = False
    
    return [i for i in range(2, n) if sieve[i] == True]

if __name__ == '__main__':
    t = int(input())


    for i in range(t):
        N = int(input())
        if N == 1:
            print(0)
        else:
            print((prime_list(N + 1))) 
            print(len(prime_list(N+1)))

