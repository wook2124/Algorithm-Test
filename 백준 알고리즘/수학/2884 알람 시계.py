# 2884번 : 알람 시계
h,m = map(int, input().split())

if m > 44:                  # 10h 45m
    print(h, m - 45)        # 10h 0m
elif h >= 1 and m <= 44:    # 23h 40m, 1h 5m
    print(h - 1, m + 15)    # 22h 55m, 1h 20m
else:                       # 0h 30m
    print(23, m + 15)       # 23h 45m