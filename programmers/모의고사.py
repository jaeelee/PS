# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    모의고사.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/30 17:11:18 by jaeelee           #+#    #+#              #
#    Updated: 2022/03/30 17:11:19 by jaeelee          ###   ########seoul.kr   #
#                                                                              #
# **************************************************************************** #

def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    cnt = [0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            cnt[0] += 1;           
        if answers[i] == b[i % len(b)]:
            cnt[1] += 1;            
        if answers[i] == c[i % len(c)]:
            cnt[2] += 1;
            
    for i in range(len(cnt)):
        if cnt[i] == max(cnt):
            answer.append(i + 1);
    return answer