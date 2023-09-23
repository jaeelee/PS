/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   1761.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/09/16 08:26:03 by jaeelee           #+#    #+#             */
/*   Updated: 2021/09/16 11:20:59 by jaeelee          ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

#include <bits/stdc++.h> // 자수 사용하는 라이브러리들을 컴파일하도록 함
using namespace std;

// vector<vector<int[2]> > graph;

/**
 * @brief   dfs 탐색 알고리즘
 * @param   graph : 탐색할 그래프
 * @param   start : 탐색 시작 번호
 */
vector<int> dfs(vector<int> graph[], int start)
{
    vector<int> visited;
    vector<int> s;
    
    int n;
    
    s.push_back(start);

    while (!s.empty())
    {
        n = s.back();
        s.pop_back();
        
        if (find(visited.begin(), visited.end(), n) == visited.end())
        {
            visited.push_back(n);
            s.insert(s.end(), graph[n].begin(), graph[n].end());
        }
    }

    return visited;
}

/**
 * @brief   주어진 두 정점 사이의 거리를 구하기
 */
int main()
{
    int n;
    int m;
    int a, b, w;
    cin >> n;
    
    vector<int> graph[n + 1];
    int weight[n + 1][n + 1];
    
    for (int i = 0; i < n - 1; i++)
    {
        cin >> a >> b >> w;
        graph[a].push_back(b);
        graph[b].push_back(a);
        weight[a][b] = w;
        weight[b][a] = w;
    }

    cin >> m;
    for (int i = 0; i < m; i++)
    {
        cin >> a >> b;
        //
        vector<int> v = dfs(graph, a);
        for (int i = 0; i < v.size(); i++)
        {
            cout << v[i] << " ";
        }
    }
}