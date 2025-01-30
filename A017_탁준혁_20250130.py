n = input()  # 방 번호 입력
numbers = [0] * 10  # 0부터 9까지 각 숫자의 개수를 저장할 리스트

# 각 숫자의 개수 세기
for digit in n:
    num = int(digit)
    # 6과 9는 같이 처리
    if num == 9:
        numbers[6] += 1
    else:
        numbers[num] += 1

# 6과 9는 서로 바꿔 쓸 수 있으므로 2로 나누고 올림
numbers[6] = (numbers[6] + 1) // 2

# 가장 많이 필요한 숫자의 개수가 필요한 세트의 개수
print(max(numbers))