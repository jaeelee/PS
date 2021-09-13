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