def solution(cards1, cards2, goal):
    answer = ''
    card1_index = 0
    card2_index = 0
    
    for g in goal:
        if g in cards1:
            if g == cards1[card1_index]:
                card1_index += 1
                continue
            else:
                return "No"
        
        if g in cards2:
            if g == cards2[card2_index]:
                card2_index += 1
                continue
            else:
                return "No"
    
    return "Yes"