n = int(input())
first = int(input())

# N이 6 이상이면 불가능
if n >= 6:
    print("Love is open door")
else:
    # N이 6 미만인 경우는 단순히 번갈아가면서 출력
    for i in range(2, n+1):
        first = 1 - first  # 0을 1로, 1을 0으로 변환
        print(first)