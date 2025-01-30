num = list(map(int, input().split(" ")))

answer = 0
for n in num:
    answer += n**2

print(answer%10)