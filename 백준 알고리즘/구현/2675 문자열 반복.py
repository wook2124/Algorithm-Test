# 2675번 : 문자열 반복
t = int(input())            # t = 2

for _ in range(t):
    r, s = input().split()  # r = 3, s = ABC
    p =""
    for i in s:
        p += int(r) * i
    print(p)