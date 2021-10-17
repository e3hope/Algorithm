def dfs(x, y):
    stack = []
    stack.append((x, y))

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                stack.append((nx, ny))

    return maze[n - 1][m - 1]

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
print(dfs(0, 0))