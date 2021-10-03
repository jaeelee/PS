# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Weekly7.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/10/03 22:26:28 by jaeelee           #+#    #+#              #
#    Updated: 2021/10/03 22:26:30 by jaeelee          ###   ########seoul.kr   #
#                                                                              #
# **************************************************************************** #

def solution(enter, leave):
    answer = [0 for i in range(len(enter))]
    meeting_room = []
    
    j = 0
    for i in range(len(enter)):
        meeting_room.append(enter[i])
        while j < len(leave) and leave[j] in meeting_room:
            meeting_room.remove(leave[j])
            for k in meeting_room:
                answer[k - 1] += 1
            answer[leave[j] - 1] += len(meeting_room)
            j += 1
        
    return answer