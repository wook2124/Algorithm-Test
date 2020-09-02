N = int(input())        # 68
ls = N
ln = 0                  # 싸이클 수

while(True):
    a = ls // 10        # 6
    b = ls % 10         # 8
    c = (a + b) % 10    # 6 + 8 = 1"4"
    ls = (b * 10) + c   # 8 + 4 = 84

    ln = ln + 1         # 싸이클 수 + 1
    if(ls == N):        # ls에서 68 숫자가 나오면 멈춤
        break

print(ln)