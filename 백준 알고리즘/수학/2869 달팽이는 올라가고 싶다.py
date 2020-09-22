# 2869번 : 달팽이는 올라가고 싶다
'''
# 시간초과한 코드
a, b, v = map(int, input().split())
day = 0

while 1:
    if a - b == v:
        print(day)
        break
    a += 2
    b += 1
    day += 1
'''
# 통과한 코드
a, b, v = map(int, input().split())
day = (v - b) / (a - b)     # (a * day) - (b * (day - 1)) >= v

print(int(day) if day == int(day) else int(day) + 1)