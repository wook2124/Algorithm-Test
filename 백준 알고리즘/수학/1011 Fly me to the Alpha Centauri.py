# 1011번: Fly me to the Alpha Centauri
t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    dist = y - x
    cnt = 1
    while 1:
        if cnt ** 2 <= dist < (cnt + 1) ** 2:
            break
        cnt += 1
    if cnt ** 2 == dist:
        print((cnt * 2) - 1)
    elif cnt ** 2 < dist <= cnt ** 2 + cnt:
        print(cnt * 2)
    else:
        print((cnt * 2) + 1)