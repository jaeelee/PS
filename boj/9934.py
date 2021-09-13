# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    9934.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/17 18:59:28 by jaeelee           #+#    #+#              #
#    Updated: 2021/09/09 22:21:04 by jaeelee          ###   ########seoul.kr   #
#                                                                              #
# **************************************************************************** #

def tree(k, s):
    n = int(len(s) / 2)
    if len(s) == 1:
        ans[k - 1].append(s[0])
    else: 
        ans[k - 1].append(s[n])
        tree(k - 1, s[:n])
        tree(k - 1, s[n + 1:])



if __name__ == '__main__':
    k = int(input())
    s = input().split(' ')
    ans = [[] for i in range(k)]
    tree(k, s)
    for i in reversed(range(k)):
        print(*ans[i])
