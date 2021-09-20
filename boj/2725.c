/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   2725.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/09/20 11:48:15 by jaeelee           #+#    #+#             */
/*   Updated: 2021/09/20 13:07:10 by jaeelee          ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

/**
 * @brief	유클리드 호제법을 사용한 최대공약수를 구하는 알고리즘
 * @details	b가 0이면 a를 리턴, 0이 아니면 b와 'a를 b로 나눈 나머지'에 대해서 다시 수행
 */
int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }


/**
 * @brief	기울기의 개수구하기
 * @param	N : 0 <= x,y <= N
 */
void	count_slope(int s_cnt[], int N)
{
	int x, y;
	int cnt;

	if (N == 0)
		return ;
	
	count_slope(s_cnt, N - 1);

	cnt = 0;
	for (x = 0; x <= N; x++)
		if (gcd(x, N) == 1)
			cnt++;

	for (y = 0; y < N; y++)
		if (gcd(y, N) == 1)
			cnt++;
	
	s_cnt[N] = s_cnt[N - 1] + cnt;
}


/**
 * @brief	서로 다른 기울기를 가지는 직선의 개수를 구하는 문제
 * @param	C : 테스트 케이스의 개수
 * @param	N : 0 <= x,y <= N
 */
int	main()
{
	int C;
	int N[1001];
	int max;
	int *slope_cnt;
	int	s_cnt[1001] = {0,};

	scanf("%d", &C);
	max = 0;
	for (int i = 0; i < C; i++)
	{
		scanf("%d", &N[i]);
		if (max < N[i])
			max = N[i];
	}

	count_slope(s_cnt, max);
	for (int i = 0; i < C; i++)
		printf("%d\n", s_cnt[N[i]]);
}