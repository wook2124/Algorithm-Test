N = input()    # "26"
n = N
cnt = 0

while 1:
   if len(n) == 1:
      n = "0" + n
   plus = str(int(n[0]) + int(n[1]))   # 2 + 6 = "8"
   n = n[-1] + plus[-1]    # "6" + "8" = "68"
   cnt += 1
   if n == N:
      print(cnt)
      break
