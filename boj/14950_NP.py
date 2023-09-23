#!/usr/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    14950.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/09/16 12:30:12 by jaeelee           #+#    #+#              #
#    Updated: 2021/09/16 13:28:02 by jaeelee          ###   ########seoul.kr   #
#                                                                              #
# **************************************************************************** #

"""
    최소 신장 트리(MST)중  Prim algorithm을 사용하는 문제
"""

def prim(graph, x):
    '''
        최소신장트리 중 시작 정점에서부터 출발하여 신장트리 집합을 단계적으로 확장 해나가는 방법

        args:
            graph(int[][]): 그래프의 가중치
            x(int): 시작 노드
    '''

    mst_set = set([x])
    n = len(graph) - 1
    dist = [float('inf')] * n

    # while (len(mst_set) < n):
    #     m = 999999
    #     for i in range(1, len(graph[x])):
    #         if i in mst_set:
    #             continue
    #         if  m > graph[x][i] and graph[x][i] > 0:
    #             next = i
    #     mst_set.append(next)
    #     x = next




if __name__ == '__main__':
    info = input().split(' ')
    n, m, t = [int(i) for i in info]

    graph = [[float('inf') for i in range(n + 1)] for j in range(n + 1)]
    for i in range(m):
        a, b, w = [int(i) for i in input().split(' ')]
        graph[a][b] = w
        graph[b][a] = w
        
    prim(graph, 1)
    # print(graph)