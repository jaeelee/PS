# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    k번째수.Py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/27 23:38:49 by jaeelee           #+#    #+#              #
#    Updated: 2022/03/27 23:38:49 by jaeelee          ###   ########seoul.kr   #
#                                                                              #
# **************************************************************************** #

def solution(array, commands):
    answer = []
    
    for command in commands:
        arr = array[command[0] - 1 : command[1]]
        arr.sort();
        answer.append(arr[command[2] - 1])
    return answer