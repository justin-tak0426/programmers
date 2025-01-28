def solution(t, p):
    answer = 0
    t_list = []
    
    for i in range(len(t)-len(p)+1):
        t_list.append(t[i:i+len(p)])
    
    for tl in t_list:
        if int(tl) <= int(p):
            answer += 1
    
    return answer