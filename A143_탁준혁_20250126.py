# solution = lambda s: (s.count('(') == s.count(')')) & (s[0] == '(') & (s[-1] == ')')

def solution(s):
    answer = False
    
    con_a = (s.count('(') == s.count(')')) & (s[0] == '(') & (s[-1] == ')')
    
    a = 0
    b = 0
    
    for i in s:
        if i=='(':
            a += 1
        else:
            b += 1
        
        if a < b:
            return False
    
    return con_a