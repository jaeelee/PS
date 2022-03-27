# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    네트워크.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/28 00:21:51 by jaeelee           #+#    #+#              #
#    Updated: 2022/03/28 00:21:51 by jaeelee          ###   ########seoul.kr   #
#                                                                              #
# **************************************************************************** #


# https://codlingual.tistory.com/183 참고
# 0번째 컴퓨터부터 시작하여 연결된 모든 컴퓨터를 방문
# 방문하지 않은 컴퓨터가 있으면 네트워크 개수를 증가 시키고
# 방문하지 않은 컴퓨터 중 작은 수의 컴퓨터부터 
# 다시 dfs로 연결된 컴퓨터를 방문
# 모든 컴퓨터를 방문하면 종료

def dfs(graph, start, visited):
    visited[start] = True
    
    for i in range(len(graph[start])):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, i, visited)
            
            
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            answer += 1
    
    return answer