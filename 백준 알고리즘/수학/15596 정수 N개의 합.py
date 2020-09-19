# 15596번 : 정수 N개의 합
a = [1, 2, 3, 4, 5]

def solve(a):
    ans = 0
    for i in a:
        ans += i
        
    print(ans)

solve(a)
