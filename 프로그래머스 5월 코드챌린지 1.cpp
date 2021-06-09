/*
    약수의 개수가 짝수이면 더하고 훌수이면 빼기
*/

/*
    완전 탐색을 이용한 방법
*/
#include <string>
#include <vector>

using namespace std;

int cnt_divisor(int n)
{
    int cnt = 0;
    for (int i = 1; i <= n; i++)
    {
        if (n % i == 0)
            cnt ++;
    }
    return (cnt);
}

int solution(int left, int right) {
    int answer = 0;
    
    for (int i = left; i <= right; i++)
    {
        if (cnt_divisor(i) % 2 == 0)
            answer += i;
        else
            answer -= i;
    }
    
    return answer;
}

//////////////////////////////////////////////

/*
    제곱수를 이용한 방법
*/
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int sum_natural_number(int x)
{
    return (x * (x + 1) / 2);
}

int sum_square_number(int x)
{
    return (x * (x + 1) * (2 * x + 1) / 6);
}

int solution(int left, int right) {
    int answer = 0;

    answer += sum_natural_number(right) - sum_natural_number(left - 1);
    answer -= 2 * (sum_square_number(sqrt(right)) - sum_square_number(sqrt(left - 1)));

    return answer;
}