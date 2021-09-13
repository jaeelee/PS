/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   17834.cpp                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/09/06 08:42:58 by jaeelee           #+#    #+#             */
/*   Updated: 2021/09/06 10:29:26 by jaeelee          ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define MAX_LEN 500001

/**
 * @brief	bfs의 기본 형태
 */
// void	bfs(vector<int> graph[], int v)
// {
// 	queue<int> node;
// 	int visit[MAX_LEN];
// 	visit[v] = 1;
// 	node.push(v);

// 	while (!node.empty())
// 	{
// 		v = node.front();
// 		node.pop();
// 		for (int i = 0; i < graph[v].size(); i++)
// 		{
// 			if (visit[graph[v][i]] == 0)
// 			{
// 				visit[graph[v][i]] = 1;
// 				node.push(graph[v][i]);
// 			}
// 		}
// 	}
// }

/**
 * @brief	bfs를 이용한 그래프를 두가지 색상으로 색칠하는 방법이다.
 * @details	정점의 색상을 1(or RED)로 칠한 후 인접한 정점은 자신과 다른 색상으로 칠한다.
 */
int	bipartite_bfs(vector<int> graph[], int v)
{
	queue<int> node;
	int visit[MAX_LEN];
	int color = 1;
	int cnt_color[3];
	visit[v] = color;
	cnt_color[color]++;
	node.push(v);

	while (!node.empty())
	{
		v = node.front();
		node.pop();
		if (visit[v] == 1)
			color = 2;
		else
			color = 1;
		for (int i = 0; i < graph[v].size(); i++)
		{
			if (visit[graph[v][i]] == 0)
			{
				visit[graph[v][i]] = color;
				node.push(graph[v][i]);
				cnt_color[color]++;
			}
			else if (visit[graph[v][i]] == visit[v])
				return (0);
		}
	}
	
	return (cnt_color[1] * cnt_color[2] * 2);
}

int		main()
{
	int n, m;
	int u, v;
	cin >> n >> m;
	vector<int> graph[n + 1];

	for (int i = 0; i < m; i++)
	{
		cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	cout << bipartite_bfs(graph, 1);
}