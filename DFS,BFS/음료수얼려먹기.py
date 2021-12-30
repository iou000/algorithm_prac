n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
#-----------------입력받기------------------

def dfs(x,y):
    stack= []
    stack.append([x,y])

    dx = [-1,0,1,0] # 상 하 좌 우
    dy = [0,-1,0,1]

    while stack: # 스택이 빌 때까지 반복
        v = stack.pop()
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m: # 범위를 벗어날 경우
                continue

            if graph[nx][ny] == 0:
                stack.append([nx,ny])
                graph[nx][ny] = 1

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i,j)
            result += 1
print(result)