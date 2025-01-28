def solution(wallpaper):
    answer = []
    l = 99
    r = -1
    u = 99
    d = -1
    
    for h, wp in enumerate(wallpaper,0):
        for idx in range(len(wp)):
            if wp[idx] == '.':
                continue
            
            if h < u:
                u = h
            if idx < l:
                l = idx
            if idx > r:
                r = idx
            if h > d:
                d = h
    
    answer = [u, l, d+1, r+1]   
    
    return answer