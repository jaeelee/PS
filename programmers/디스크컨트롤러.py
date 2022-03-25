# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    디스크컨트롤러.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/25 21:35:12 by jaeelee           #+#    #+#              #
#    Updated: 2022/03/25 21:35:12 by jaeelee          ###   ########seoul.kr   #
#                                                                              #
# **************************************************************************** #

import math
from queue import PriorityQueue


def solution(jobs):
    total = 0
    jobs_cnt = len(jobs)
    
    # 요청 순으로 정렬
    jobs.sort(key=lambda x:(x[0], x[1]))
    
    que = PriorityQueue()
    time = jobs[0][0]
    while True:
        if not jobs and que.qsize() == 0 :
            break
        if jobs and jobs[0][0] < time: # 작업 중 요청이 들어온 경우
            que.put([jobs[0][1], jobs[0][0]]) # 작업시간이 작은 순서대로 우선순위 큐에 삽입
            del jobs[0]
        elif que.qsize() > 0: # 우선순위 큐에 작업이 있는 경우(대기중인 작업이 있는 경우)
            job = que.get()
            time += job[0]
            total += time - job[1]
        else : # 대기중인 작업이 없는 경우
            time += jobs[0][1]
            total += time - jobs[0][0]
            del jobs[0]


    
    return math.trunc(total / jobs_cnt)