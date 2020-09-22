# 10250번 : ACM 호텔
t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())     # 6 12 10
    floor = n % h                           # 10 % 6 = 4 (나머지)
    distance = (n // h) + 1                 # (10 // 6) + 1 = 2 (몫)
    
    if floor == 0:                          # 6 12 18
        distance -= 1
        floor = h
    
    print(floor * 100 + distance)