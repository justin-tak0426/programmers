def solution(babbling):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        # 연속된 같은 발음이 있는지 확인
        if "ayaaya" in word or "yeye" in word or "woowoo" in word or "mama" in word:
            continue
            
        # 각 발음을 특별한 문자로 치환 (길이 1의 문자로)
        temp = word
        for idx, speak in enumerate(can_speak):
            # 각 발음을 숫자로 치환 (예: "aya" -> "1")
            temp = temp.replace(speak, str(idx))
        
        # 치환 후 숫자만 있다면 발음 가능한 단어
        if temp.isdigit():
            answer += 1
            
    return answer