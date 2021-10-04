# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Weekly8.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/10/04 23:11:14 by jaeelee           #+#    #+#              #
#    Updated: 2021/10/04 23:13:47 by jaeelee          ###   ########seoul.kr   #
#                                                                              #
# **************************************************************************** #

"""

최소 직사각형

모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return
sizes : 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열

풀이 : 명함의 가로와 세로 중 큰 수 중 가장 큰값 * 작은 수 중 가장 큰값
"""

def solution(sizes):
    width = 0
    height = 0
    for i in sizes:
        width = max(max(i), width)
        height = max(min(i), height)
    return  width * height