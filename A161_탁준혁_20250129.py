def solution(keymap, targets):
    # 각 문자별 최소 키 입력 횟수를 저장할 딕셔너리
    char_min_presses = {}
    
    # keymap을 순회하면서 각 문자별 최소 입력 횟수 계산
    for key in keymap:
        for i, char in enumerate(key, 1):  # 1부터 시작하는 인덱스 사용
            # 해당 문자의 현재 최소 입력 횟수와 비교하여 더 작은 값 저장
            if char not in char_min_presses or char_min_presses[char] > i:
                char_min_presses[char] = i
    
    result = []
    
    # 각 target 문자열에 대해 필요한 총 키 입력 횟수 계산
    for target in targets:
        total_presses = 0
        impossible = False
        
        # 문자열의 각 문자에 대해 필요한 키 입력 횟수 더하기
        for char in target:
            if char not in char_min_presses:
                impossible = True
                break
            total_presses += char_min_presses[char]
        
        # 불가능한 경우 -1, 가능한 경우 총 키 입력 횟수 추가
        result.append(-1 if impossible else total_presses)
    
    return result