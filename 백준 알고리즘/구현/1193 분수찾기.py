# 1139번 : 분수찾기
x = int(input())        # x = 14
line = 1

while x > line:
    x -= line           # x = 14, 13, 11, 8, 4
    line += 1           # line = 1, 2, 3, 4, 5

if line % 2 == 0:       
    a = x               
    b = line - x + 1
else:
    a = line - x + 1
    b = x

print(a, "/", b, sep = "")