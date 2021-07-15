"""
N x M 직사각형 형태의 미로에 갇혀있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
동빈이의 위치는 (1,1)이고 미로의 출구는 (N,M)의 위치에 조냊하며 한 번에 한 칸씩 이동할 수 있다.
이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 
미로는 반드시 탈출할 수 있는 형태로 제시된다.
이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다. 

입력
첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (4 <= N,M <= 200)
다음 N개의 줄에는 각각 M개의 정수로 미로의 정보가 주어진다. 각각의 수는 공백없이 붙어서 입력으로 제시된다.
또한 시작 칸과 마지막 칸은 항상 1 이다.

출력 
최소 이동 칸의 개수를 출력
"""
# BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하므로, BFS 활용
from collections import deque

N, M = map(int, input().split())

maze = []
for i in range(N):
    maze.append(list(map(int, input())))

# 상하좌우 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0,0))

while queue:
    x, y = queue.popleft()
    # 현재 위치에서 네 방향으로의 위치 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if maze[nx][ny] == 0:
            continue
        # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx,ny))
# BFS를 수행한 후, 마지막 탈출구에 있는 숫자 출력
print(maze)
print(maze[N-1][M-1])