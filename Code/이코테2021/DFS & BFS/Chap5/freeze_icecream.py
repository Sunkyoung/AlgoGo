


N, M = map(int, input().split())

tray = []
for i in range(N):
    tray.append(list(map(int, input())))
print(tray)
def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if tray[x][y] == 0:
        tray[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)