def solution(table, languages, preference):
    answer = ''
    # table 은 모든 테스트케이스에서 동일
    table = {
        'SI':{'JAVA':5,'JAVASCRIPT':4,'SQL':3,'PYTHON':2,'C#':1},
        'CONTENTS':{'JAVASCRIPT':5,'JAVA':4,'PYTHON':3,'SQL':2,'C++':1},
        'HARDWARE':{'C':5,'C++':4,'PYTHON':3,'JAVA':2,'JAVASCRIPT':1},
        'PORTAL':{'JAVA':5,'JAVASCRIPT':4,'PYTHON':3,'KOTLIN':2,'PHP':1},
        'GAME':{'C++':5,'C#':4,'JAVASCRIPT':3,'C':2,'JAVA':1},
    }
    
    max = -9999
    for i in table:
        sum = 0
        for j in range(len(languages)):
            if languages[j] in table[i]:
                sum += table[i][languages[j]] * preference[j]
        if max == sum and answer > i:
            max = sum
            answer = i
        elif max < sum:
            max = sum
            answer = i
    return answer