# https://www.acmicpc.net/problem/2845
# solved July 6 2020
# Sunkyoung Kim

l, p = input().split()
participants = input().split()

for pa in participants:
	print(int(pa)  - int(l)*int(p), end=' ')