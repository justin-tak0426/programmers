def solution(array, commands):
    answer = []
    
    for cmd in commands:
        i = cmd[0]
        j = cmd[1]
        k = cmd[2]
    
        n_array = array[i-1:j]
        n_array.sort()
        answer.append(n_array[k-1])
    
    
    return answer