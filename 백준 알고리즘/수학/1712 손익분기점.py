# 1712번 : 손익분기점
a, b, c = map(int, input().split())     # 고정비용, 가변비용, 판매비용
e = 0

if c <= b:  # 판매비용이 가변비용과 같거나 작아지면 이익이 없어지는 것임
    print(-1)
else:
    print(int(a / (c - b)) + 1)         # int를 안붙이면 11.0으로 출력됨