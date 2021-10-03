# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    모두0으로만들기.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/09/24 18:44:55 by jaeelee           #+#    #+#              #
#    Updated: 2021/09/24 18:44:57 by jaeelee          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
	프로그래머스 4월 코드챌린지 문제

    트리의 모든 점의 가중치를 0으로 만들기
    임의의 연결된 두 점을 골라서 한쪽은 1증가시키고, 다른 한쪽은 1 감소시킨다.
"""


import sys
sys.setrecursionlimit(300000) # 재귀 깊이 제한 참고 : https://fuzzysound.github.io/sys-setrecursionlimit


def dfs(a, graph, start, visited):
	global answer
	visited[start] = 1
	ret = 0
	for i in graph[start]:
	if visited[i] == 1:
	continue
	if len(graph[i]) != 1: # 리프노드가 아닐 경우
	dfs(a, graph, i, visited)
	answer += abs(a[i])
	a[start] += a[i]
	a[i] = 0


	def solution(a, edges):
		global answer
		answer = 0
		visited = [0 for i in range(len(a))]
		graph = [[] for i in range(len(a))]
		if sum(a) != 0:
		return -1

		for i in range(len(edges)):
	graph[edges[i][0]].append(edges[i][1])
	graph[edges[i][1]].append(edges[i][0])

	dfs(a, graph, 0, visited)
	return answer
