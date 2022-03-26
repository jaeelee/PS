/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   완주하지 못한 선수.cpp                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/26 17:36:24 by jaeelee           #+#    #+#             */
/*   Updated: 2022/03/26 17:36:24 by jaeelee          ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    
    for (int i = 0; i < participant.size(); i++)
    {
        if (i >= completion.size())
            answer = participant[i];
        else if (participant[i].compare(completion[i]) != 0)        
        {
            answer = participant[i];
            break;
        }
    }
    return answer;
}

/* 수정 답안
string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    
    for (int i = 0; i < completion.size(); i++)
    {
        if (participant[i].compare(completion[i]) != 0)        
            return participant[i];
    }
    return participant[completion.size()];
}

*/