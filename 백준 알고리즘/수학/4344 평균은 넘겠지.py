# 4344번 : 평균은 넘겠지
c = int(input())
avg = []

for _ in range(c):
    n = list(map(int, input().split()))

    sum = 0
    for i in range(n[0]):   # n = [5, 50, 50, 70, 80, 100]
        sum += n[i + 1]     # sum = 350
    
    cnt = 0                 # 평균을 넘는 학생들
    for i in range(n[0]):   # sum / n[0] = 70
        if n[i + 1] > (sum / n[0]):
            cnt += 1
            
    avg.append((cnt / n[0]) * 100)
    n.clear()               # 입력받는 n 리스트 초기화

for i in range(c):
    print("%.3f" %avg[i] + "%")