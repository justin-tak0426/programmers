def solution(s):
    answer = []
    s_dict = {}
    
    for i in range(len(s)):
        try:
            answer.append(i - s_dict[s[i]])
            s_dict[s[i]] = i
        except:
            s_dict[s[i]] = i
            answer.append(-1)
    
    return answer