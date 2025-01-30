from collections import Counter

def solution(participant, completion):
    # Counter 객체로 변환하여 뺄셈
    answer = Counter(participant) - Counter(completion)
    # 남은 한 명의 이름 반환
    return list(answer.keys())[0]