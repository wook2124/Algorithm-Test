# 2292번 : 벌집
n = int(input())        # n = 13
num = 1                 # 첫 번째 숫자
cnt = 6                 # 증가하는 등차수열
room = 1                # 지나가는 방의 수

if n == 1:
    print(1)
else:
    while True:
        num = num + cnt
        room += 1
        if n <= num:
            print(room)
            break
        cnt += 6