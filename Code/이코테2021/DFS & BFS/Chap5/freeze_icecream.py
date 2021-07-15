# 연결 요소 찾기 문제의 유형
"""
N x M 크기의 얼음 틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 
구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때, 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N,M <= 1000)
두 번재 줄부터 N+1 줄까지 얼음 틀의 형태가 주어진다.
이 때, 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

출력 
한번에 만들 수 있는 아이스크림의 개수를 출력한다.
"""

N, M = map(int, input().split())

tray = []
for i in range(N):
    tray.append(list(map(int, input())))

def dfs(x, y):
    # 주어진 범위를 벗어날 경우, 즉시 종료
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if tray[x][y] == 0:
        # 해당 노드 방문 처리
        tray[x][y] = 1
        # 상, 하, 좌, 우 위치들도 재귀적으로 호출
        # return 값 없이 방문 처리만 수행
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 dfs 수행
        if dfs(i, j) == True:
            result += 1

print(result)