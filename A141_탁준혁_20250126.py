def solution(phone_book):
    answer = True    
    s_b = sorted(phone_book)
    for j in range(len(s_b)-1):
        if s_b[j+1].startswith(s_b[j]):
            return False
        
    return answer