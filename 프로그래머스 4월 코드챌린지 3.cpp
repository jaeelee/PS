/*
    트리의 모든 점의 가중치를 0으로 만들기
    임의의 연결된 두 점을 골라서 한쪽은 1증가시키고, 다른 한쪽은 1 감소시킨다.
*/

#include <bits/stdc++.h> // 자수 사용하는 라이브러리들을 컴파일하도록 함
using namespace std;

long long answer = 0;
vector<vector<int>> map;
vector<long long> weight;
vector<int> visited;

void dfs(int x, int top)
{
    for (int i : map[x])
    {
        if (i == top) continue; // 위치 중요!
        if (map[i].size() != 1) dfs(i, x); // 위치 중요!
        answer += abs(weight[i]);
        weight[x] += weight[i];
        weight[i] = 0;
    }
}

long long solution(vector<int> a, vector<vector<int>> edges) {
    int i;
    int sum;

    visited.assign(a.size(), 0);
    map.assign(a.size(), vector<int> (0));
    for (int i : a) weight.push_back((long long)i);
    sum = 0;
    i = -1;
    while (++i < a.size())
        sum += a[i];
    if (sum != 0)
        return (-1);

    i = -1;
    while (++i < edges.size())
    {
        map[edges[i][0]].push_back(edges[i][1]);
        map[edges[i][1]].push_back(edges[i][0]);
    }

    dfs(0, -1);
    return answer;
}