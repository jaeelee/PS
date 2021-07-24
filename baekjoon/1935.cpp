/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/07/25 04:33:48 by jaeelee           #+#    #+#             */
/*   Updated: 2021/07/25 05:39:43 by jaeelee          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <iomanip>
#include <string>
#include <stack>
using namespace std;

double calc(char op, stack<double> *s)
{
	double b = s->top();
	s->pop();
	double a = s->top();
	s->pop();

	if (op == '+')
		return (a + b);
	else if (op == '-')
		return (a - b);
	else if (op == '*')
		return (a * b);
	else if (op == '/')
		return (a / b);
	return (0);
}

int	main()
{
	int N;
	int num[26] = {0,};
	stack<double> s;
	string str;
	string tmp;

	cin >> N;
	cin >> str;
	for(int i = 0; i < N; i++)
		cin >> num[i];

	for (int i = 0; i < str.size(); i++)
	{
		if (str[i] >= 'A' && str[i] <= 'Z')
			s.push(num[str[i] - 'A']);
		else
			s.push(calc(str[i], &s));
	}

	cout << fixed << setprecision(2) << s.top();
	return (0);
}
