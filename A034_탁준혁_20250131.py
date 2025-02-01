# 나머지를 저장할 집합(set) 생성
remainders = set()

# 10개의 수를 입력받아 각각 42로 나눈 나머지를 집합에 추가
for _ in range(10):
    num = int(input())
    remainders.add(num % 42)

# 집합의 크기(서로 다른 나머지의 개수) 출력
print(len(remainders))