# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    추석트래픽.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/10/03 22:25:52 by jaeelee           #+#    #+#              #
#    Updated: 2021/10/03 22:25:53 by jaeelee          ###   ########seoul.kr   #
#                                                                              #
# **************************************************************************** #

# from datetime import datetime
import datetime
"""
    그리드의 활동 선택 문제 응용
"""

def get_time(date, time):
    ''' get_time
    날짜와 시간 문자열을 받아와서 datetime 타입으로 변환
    
    args:
        date(str): 날짜 문자열
        time(str): 시간 문자열
    '''
    date_str = date + " " + time
    date_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
    
    return (date_time)


def solution(lines):
    ''' solution
    초당 최대 처리량을 구하는 함수. (그리디 알고리즘 - 활동 선택 문제 응용)
    args:
        lines(string): 로그 문자열. 응답완료시간(S)와 처리시간(T)가 공백으로 구분되어있다.
            2016-09-15 hh:mm:ss.sss 형식
            T는 0.312s와 같이 최대 소수점 셋째 자리까지 기록
            0.001 <= T <= 3.000
            
    retuern(int): 초당 최대 처리량(응답 완료 여부에 관계없이 임의 시간부터 1초(=1,000밀리초)간 처리하는 요청의 최대 개수)
    '''
    answer = 0
    
    cnt = 0
    throughput = 0
    start_time = []
    end_time = []
    
    for i in lines:
        info_i = i.split()
        sec = float(info_i[2][:-1]) - 0.001
        start_time.append(get_time(info_i[0], info_i[1]) - datetime.timedelta(seconds=sec))
        end_time.append(get_time(info_i[0], info_i[1]) + datetime.timedelta(seconds=1))
        
    for i in range(len(lines)):
        cnt += 1
        throughput = 0
        
        for j in range(i, len(lines)):
            if (start_time[j] < end_time[i]):
                throughput += 1
        answer = max(answer, throughput)
    
    return answer