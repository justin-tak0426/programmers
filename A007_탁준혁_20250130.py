# 입력 받고 정수로 변환
num = list(map(int, input().split()))

# 원본 리스트를 저장
original = num[:]

# 오름차순, 내림차순 정렬된 리스트 생성
ascending = sorted(num)
descending = sorted(num, reverse=True)

# 비교
if original == ascending:
    print("ascending")
elif original == descending:
    print("descending")
else:
    print("mixed")