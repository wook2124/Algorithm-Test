# 1002번 : 터렛
t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

    # 같은 점일때: -1 or 0
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
    
    # distance(점 사이의 거리)가 반지름 더한 값보다 작을 때: 0
    # 한 원이 다른 원을 포함하도록 클 때: 0
    if r1 > (distance + r2) or r2 > (distance + r1) or distance > (r1 + r2):
        print(0)
    
    # 외접하거나 내접할 때: 1
    elif r1 == (distance + r2) or r2 == (distance + r1) or (r1 + r2) == distance:
        print(1)
    
    # 그 외: 2
    else:
        print(2)