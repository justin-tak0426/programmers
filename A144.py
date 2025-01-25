def solution(word):
    vowels = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    weights = [781, 156, 31, 6, 1]  # 5^4 + 5^3 + 5^2 + 5^1 + 5^0, 5^3 + 5^2 + 5^1 + 5^0, ...
    answer = len(word)  # 글자 수만큼 기본값
    for i, char in enumerate(word):
        answer += vowels[char] * weights[i]
    
    return answer