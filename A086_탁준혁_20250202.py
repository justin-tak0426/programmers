def get_english(n):
   nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
   if n < 10:
       return nums[n]
   return nums[n//10] + ' ' + nums[n%10]

m, n = map(int, input().split())
nums = []

for i in range(m, n+1):
   nums.append((get_english(i), i))

nums.sort()
count = 0

for _, num in nums:
   print(num, end=' ')
   count += 1
   if count % 10 == 0:
       print()

if count % 10 != 0:
   print()