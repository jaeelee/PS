/*
    x(이진수)보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은수
*/

#include <string>
#include <vector>
#include <iostream>
using namespace std;

long long ft_pow(long long x, long long y)
{
    long long i = -1;
    long long n = 1;
    while (++i < y)
        n *= x;
    return (n);
}

long long f(long long x)
{
    string s;
    long long n = 0;
    long long cnt = 0;
    long long i = 0;
    int flag = -1;
    
    while (x != 0)
    {
        if (x % 2 == 0 && flag == -1)
        {
            flag = cnt;
            s += "1";
        }
        else
            s += (x % 2 == 0 ? "0" : "1");
        cnt++;
        x /= 2;
    }
    if (flag == -1)
    {
        flag = s.size();
        s += "1";
    }
    while (--flag >= 0)
    {
        if (s[flag] == '1')
        {
            s[flag] = '0';
            break ;
        }
    }
    while (i < s.size())
        n += (s[i] - '0') * ft_pow(2, i++);
    return n;
}

vector<long long> solution(vector<long long> numbers) {
    vector<long long> answer;
    
    for (long long i = 0; i < numbers.size(); i++)
        answer.push_back(f(numbers[i]));
    
    return answer;
}

/////////////////////////////////

/*
    비트 연산을 이용한 방법
    C언어
*/
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
long long* solution(long long numbers[], size_t numbers_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    long long* answer = (long long*)malloc(sizeof(long long ) * numbers_len);
    int j;
    
    for (int i = 0; i < numbers_len; i++) 
    {
        for (j = 0; j < 64; j++)// long long 은 64bit
        {
            if ((numbers[i] & (1LL << j)) == 0)
            {
                numbers[i] ^= (1LL << j);
                break ;
            }
        }
        while (--j >= 0)
        {
            if ((numbers[i] & (1LL << j)) >= 1)
            {
                numbers[i] ^= (1LL << j);
                break ;
            }
        }
        answer[i] = numbers[i];
    }
    
    return answer;
}