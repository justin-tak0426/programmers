def solution(food):
    answer = ''
    length = 0
    
    for i in range(1, len(food)):
        tmp_n = int(food[i])//2
        for _ in range(tmp_n):
            answer += str(i)
            length += 1
    
    answer += '0'
    
    for i in range(1, length+1):
        answer += answer[length-i]
    
    
    
    return answer