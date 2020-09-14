'''
[문제설명]
직사각형을 만드는 데 필요한 4개의 점 중 3개의 좌표가 주어질 때
나머지 한 점의 좌표를 구하려고 합니다.

점 3개의 좌표가 들어있는 배열 v가 매개변수로 주어질 때
직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 return 하도록 
solution 함수를 완성해주세요.

단, 직사각형의 각 변은 x축, y축에 평행하며
반드시 직사각형을 만들 수 있는 경우만 입력으로 주어집니다.

[제한사항]
v는 세 점의 좌표가 들어있는 2차원 배열입니다.
v의 각 원소는 점의 좌표를 나타내며, 좌표는 [x축 좌표, y축 좌표] 순으로 주어집니다.
좌표값은 1 이상 10억 이하의 자연수입니다.
직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 [x축 좌표, y축 좌표] 순으로 담아 return 해주세요.
'''
def solution(v):
    answer = []
    v1 = []
    v2 = []
    for i in v:                 # v = [[1, 1], [2, 2], [1, 2]]
        if i[0] not in v1:      # 1번째 i[0] = 1, 2번째 i[0] = 2, 3번째 i[0] = 1
            v1.append(i[0])
        else:
            v1.remove(i[0])     # 중복된 1번째, 3번째 1을 remove함
        if i[1] not in v2:      # 1번째 i[1] = 1, 2번째 i[1] = 2, 3번째 i[1] = 2
            v2.append(i[1])
        else:
            v2.remove(i[1])     # 중복된 2번째, 3번째 2를 remove함
    answer = v1 + v2            # 남아있는 v1 = [2]와 v2 = [1]을 더해줌
    return answer               # [2, 1]