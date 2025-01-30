from statistics import mean

n = int(input())
num_list = []
for i in range(n):
    num_list.append(list(map(int, input().split(" "))))
    

for num in num_list:
    m = mean(num[1:])
    count = 0
    for j in num[1:]:
        if j > m:
            count += 1
    
    print(f"{count/len(num[1:])*100:.3f}%")

