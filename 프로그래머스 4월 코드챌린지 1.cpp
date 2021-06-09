/*
    정수와 부호를 담은 배열을 받아와서 합을 구하는 문제    
*/

#include <string>
#include <vector>

using namespace std;

int solution(vector<int> absolutes, vector<bool> signs) {
    int answer = 0;
    int i = -1;
    
    while (++i < absolutes.size())
    {
        if (signs[i])
            answer += absolutes[i];
        else
            answer -= absolutes[i];
    }
    return answer;
}