def solution(today, terms, privacies):
    answer = []
    
    today_list = today.split('.')
    
    today = list(map(int, today_list))
    print(today)
    today_total = (today[0]-1) * 12 * 28 + (today[1]-1) * 28 + today[2]
    
    terms_dict = {}
    for t in terms:
        tmp = t.split(' ')
        terms_dict[tmp[0]] = int(tmp[1])
    
    print(terms_dict)
    
    for idx, p in enumerate(privacies, 1):
        p = p.replace(' ','.')
        tmp = p.split('.')
        
        year = int(tmp[0])
        month = int(tmp[1])
        day = int(tmp[2])
        
        total = (year-1) * 12 * 28 + (month-1) * 28 + day
        
        tp = terms_dict[tmp[3]]
        
        if today_total - total >= tp * 28:
            answer.append(idx)
        
        
    
    return answer