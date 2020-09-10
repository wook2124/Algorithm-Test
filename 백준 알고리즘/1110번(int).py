n = int(input())        # 68
num = n
cnt = 0                  # 싸이클 수

while True:
    a = num // 10        # 6
    b = num % 10         # 8
    c = (a + b) % 10    # 6 + 8 = 1"4"
    num = (b * 10) + c   # 8 + 4 = 84

    cnt = cnt + 1         # 싸이클 수 + 1
    if(num == n):        # ls에서 68 숫자가 나오면 멈춤
        break

print(cnt)