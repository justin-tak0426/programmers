
line = []
for _ in range(4):
    line.append(list(map(int, input().split(" "))))

answer = 0

max = 0
for i in range(4):
    answer = answer - line[i][0] + line[i][1]
    if answer > max:
        max = answer

print(max)