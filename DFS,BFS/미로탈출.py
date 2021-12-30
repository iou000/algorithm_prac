from collections import deque

n, m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def bfs(x,y):
    queue = deque()
    queue.append([x-1,y-1])

    dx = [1,-1,0,0] # 동 서 남 북 방향
    dy = [0,0,1,-1]

    while queue: #큐가 빌 때 까지

        v = queue.popleft()

        for i in range(4): # 방문하지 않은 노드 탐색
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            
            if nx >= n or nx <= -1 or ny >= m or ny <= -1: # 범위를 벗어날 경우 그냥 넘어감
                continue
            
            if graph[nx][ny] == 1: # 방문하지 않은 노드라면
                queue.append([nx,ny]) # 큐에 넣어주고
                graph[nx][ny] = graph[v[0]][v[1]]+1 # 방문처리


bfs(1,1)
print(graph[n-1][m-1])


