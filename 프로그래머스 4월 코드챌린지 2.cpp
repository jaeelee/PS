/*
    대괄호, 중괄호, 소괄호로 이루어진 문자열을 왼쪽으로 x(0 <= x < 문자열의 길이)만큼 회전시켰을 때
    문자열이 올바른 괄호 문자열이 되는 경우의 개수 구하기
*/

/*
    변수를 이용한 방법
*/
#include <string>
#include <vector>

using namespace std;

int check_bracket(string s)
{
    int big = 0;
    int mid = 0;
    int small = 0;
    int i = -1;
    
    while (++i < s.length())
    {
        if (s[i] == '[')
            big++;
        else if (s[i] == ']')
            big--;
        if (s[i] == '{')
            mid++;
        else if (s[i] == '}')
            mid--;
        if (s[i] == '(')
            small++;
        else if (s[i] == ')')
            small--;
        if (big < 0 || mid < 0 || small < 0)
            break;
    }
    if (big == 0 && mid == 0 && small == 0)
        return (1);
    else
        return (0);
}

int solution(string s) {
    int answer = 0;
    int i = -1;

    while (++i < s.length())
    {
        s += s[0];
        s = s.substr(1, s.length() - 1);
        if (check_bracket(s))
            answer++;
    }
    return answer;
}


/*
    스택을 활용하는 방법
*/
#include <string>
#include <vector>
#include <stack>

using namespace std;

int check_bracket(string s)
{
    stack<char> st;
    int i = -1;

    while (++i < s.length())
    {
        if (s[i] == '[' || s[i] == '{' || s[i] == '(')
            st.push(s[i]);
        else
        {
            if (st.empty())
                return (0);
            if (s[i] == ']' && st.top() == '[')
                st.pop();
            if (s[i] == '}' && st.top() == '{')
                st.pop();
            if (s[i] == ')' && st.top() == '(')
                st.pop();
        }
    }
    if (st.empty())
        return (1);
    else
        return (0);
}

int solution2(string s) {
    int answer = 0;
    int i = -1;
    while (++i < s.length())
    {
        s += s[0];
        s = s.substr(1, s.length() - 1);
        if (check_bracket(s))
            answer++;
    }
    return answer;
}