def solution(s):
    answer = ''
    
    s = s.split(' ')
    print(type(s))
    print(s)

    for temp in s:
        temp = temp.capitalize()
            
        answer += ' ' + temp
    
    answer = answer.lstrip()
    
    return answer