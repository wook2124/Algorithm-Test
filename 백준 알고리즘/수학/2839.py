# 2839번 : 설탕 배달
n = int(input())        # 18
cnt = 0

while 1:
    if (n % 5) == 0:    # 처음엔 False
        cnt += (n // 5) # 밑에서 n - 3 이후에 15가 되어
        print(cnt)      # if가 True가 되고
        break           # n // 5의 몫인 3을 더해줌
    n -= 3              # 18 - 3 = 15
    cnt += 1
    if (n < 0):         # 만약 4 같이 -3을 했을 때 1이나오면
        print(-1)       # 0보다 적은 수가 되어 -1을 출력함
        break           # while 반복문을 멈춤