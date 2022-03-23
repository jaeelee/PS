/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   11378.cpp                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jaeelee <jaeelee@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/17 12:22:07 by jaeelee           #+#    #+#             */
/*   Updated: 2022/03/17 15:07:27 by jaeelee          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <vector>
using namespace std;

// 매칭에 성공하면 True, 실패하면 False
bool dfs(int x, vector<int> a[], bool c[], int d[])
{
	// 연결된 모든 노드에 대해서 들어갈 수 있는지 시도
	for (int i = 0; i < a[x].size(); i++)
	{
		int t = a[x][i];
		// 이미 처리한 노드는 더 이상 볼 필요 없음
		if (c[t]) continue;
		c[t] = true;

		// 비어있거나 점유 노드에 더 들어갈 공간이 있는 경우
		if (d[t] == 0 || dfs(d[t], a, c, d))
		{
			d[t] = x;
			return true;
		}
	}
	return false;
}
//bool dfs(int x, vector<int> a[], bool visit[], int b[])
//{
//	if (visit[x] == 1)
//		return false;

//	visit[x] = 1;

//	for (int i = 0; i < a[x].size(); i++)
//	{
//		if (b[i] == 0 || dfs(b[i], a, visit, b))
//		{
//			b[i] = x;
//			return true;
//		}
//	}

//	return false;

//}

int main()
{
	int N, M, K;
	scanf("%d %d %d", &N, &M, &K);
	vector<int> x[N + 1]; //  직원, N = 직원 수
	int y[M + 1]; // 할일
	bool visit[M + 1];
	int n, m;

	fill(y, y + M + 1, 0);

	// 각 지직원이 할 수 있는 일 입력
	for (int i = 1; i <= N; i++)
	{
		scanf("%d", &n);
		for (int j = 0; j < n; j++)
		{
			scanf("%d", &m);
			x[i].push_back(m);
		}
	}
	// 직원과 할일 매칭
	int cnt = 0;
	for (int i = 1; i <= N; i++)
	{
		fill(visit, visit + M + 1, false);
		if (dfs(i, x, visit, y)) cnt++;
	}


	// 남은 벌점이 있을 경우 추가 매칭
	for (int i = 1; i <= N; i++)
	{
		while (K > 0)
		{
			fill(visit, visit + M + 1, false);
			if (dfs(i, x, visit, y)){
				K--;
				cnt++;
			}
			else
				break;
		}
	}

	printf("%d", cnt);
	return 0;
}
