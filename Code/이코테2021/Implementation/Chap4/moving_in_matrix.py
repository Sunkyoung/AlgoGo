"""
NxN의 공간에서 여행가 A가 주어진 계획서에 따라 상하좌우로 이동하여 최종적으로 도착할 지점의 좌표를 찾는 문제
시작 좌표는 항상 (1,1)이다. 만약 공간을 벗어나는 움직임은 무시된다.

입력
첫째 줄에는 공간을 나타내는 N이 주어진다. (1 <= N <= 100)
둘째 줄에는 여행가 A가 이동할 계획서 내용이 주어진다. (1 <= 이동횟수 <= 100)

출력 
최종 도착 지점 좌표 (X, Y)를 공백으로 구분하여 출력
"""

N = int(input())
plan = list(input().split())

x, y = 1, 1
# direction = ['L', 'R', 'U', 'D']
# direction_point = [(0, -1), (0, 1), (-1, 0), (1, 0)]
direction = {
    'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D':(1, 0)
}

for p in plan:  
    move_x = x + direction[p][0]
    move_y = y + direction[p][1]
    if move_x > N or move_y > N or move_x < 1 or move_y < 1: # 공간을 벗어나는 경우
        continue
    x = move_x
    y = move_y

print(x, y)