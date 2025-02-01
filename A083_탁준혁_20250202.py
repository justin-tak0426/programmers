n = int(input())
nums = list(map(int, input().split()))
result = sorted(list(set(nums)))
print(*result)