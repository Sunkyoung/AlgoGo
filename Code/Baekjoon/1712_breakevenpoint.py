# https://www.acmicpc.net/problem/1712
# Solved July 7 2020
# Sunkyoung Kim

a, b, c = input().split()
if int(c) > int(b) :
    n = int(a)//(int(c)-int(b))+1
else:
    n = -1
print(n)