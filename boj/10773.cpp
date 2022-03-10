/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   10773.cpp                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/10 09:26:49 by jaeelee           #+#    #+#             */
/*   Updated: 2022/03/10 09:36:21 by jaeelee          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <stack>
using namespace std;

int main()
{
	int K;
	int n;
	int answer = 0;
	stack<int> s;

	cin >> K;

	for (int i = 0; i < K; i++)
	{
		cin >> n;
		if (n == 0)
			s.pop();
		else
			s.push(n);
	}

	while (!s.empty())
	{
		answer += s.top();
		s.pop();
	}
	cout << answer;

	return answer;
}
