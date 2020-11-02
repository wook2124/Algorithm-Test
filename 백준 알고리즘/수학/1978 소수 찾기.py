# 1978번 : 소수 찾기
n = int(input())
ls = list(map(int, input().split()))
count = 0

for i in ls:
    if i == 1:
        continue
    
    if i % 2 != 0:
        count += 1
    
print(count)