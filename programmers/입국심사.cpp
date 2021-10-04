#include <string>
#include <vector>
#include <cmath>

using namespace std;

/**
 * @brief   모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return
 * @details 이분탐색을 이용
 * @param   n 입국심사를 기다리는 사람 수
 * @param   times 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열
 */
long long solution(int n, vector<int> times) {
    long long answer = pow(10, 9) * pow(10,9); // 최악의 경우: 심사관 1명, 기다리는 사람 10^9명, 걸리는 시간 10^9
    long long start = 0;
    long long end = answer;
    
    while (start <= end)
    {
        long long mid = (start + end) / 2;;
        long long pass = 0;
        for (int i = 0; i < times.size(); i++)
            pass += mid / times[i];
        if (pass >= n)
        {
            answer = mid;
            end = mid - 1;
        }
        else
            start = mid + 1;
    }

    return answer;
}

// test 
// int main()
// {
//     vector<int> v = {7, 10};
//     cout << solution(6, v);
//     return (0);
// }