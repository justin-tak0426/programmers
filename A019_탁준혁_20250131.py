a = int(input())
b = int(input())
c = int(input())

num = [0] * 10

result = str(a*b*c)

for c in result:
    num[int(c)] += 1

for n in num:
    print(n)