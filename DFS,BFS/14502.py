# 연구소 (나의 풀이)
from collections import deque
from itertools import combinations

n,m = map(int, input().split())
graph = []
virusmap = [[0]*m for _ in range(n)] #벽을 설치한 뒤 맵 리스트
for i in range(n):
    graph.append(list(map(int, input().split())))

temp = []
for i in range(n):
    for j in range(m):
        temp.append([i,j])

wall = list(map(list,combinations(temp,3))) #벽세우기 경우의 수

def bfs(i,j,virus):
    queue = deque() # 시작위치
    queue.append([i,j])

    dx = [0, 0, -1, 1] # 상하좌우
    dy = [1, -1, 0, 0]

    while queue: # 큐가 빌 때 까지 반복
        v = queue.popleft()
        
        for i in range(4): # 인접노드 탐색
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            
            if nx >= n or nx <= -1 or ny >= m or ny <= -1: # 범위를 벗어나는 경우
                continue
            
            if virus[nx][ny] == 0: # 인접 노드의 값이 0이라면
                virus[nx][ny] = 2 # 2로 만들어줌(바이러스 감염)
                queue.append([nx,ny])

result = []
count = 0
for i in range(len(wall)):
    x1, y1 = wall[i][0] 
    x2, y2 = wall[i][1]
    x3, y3 = wall[i][2]
    
    if graph[x1][y1] == 0 and graph[x2][y2] == 0 and graph[x3][y3] == 0: # 벽은 무저건 3개 새워야함

        graph[x1][y1] = 1   # 벽을 세우고
        graph[x2][y2] = 1
        graph[x3][y3] = 1

        for i in range(n):
            for j in range(m):
                virusmap[i][j] = graph[i][j]

        for i in range(n):   # bfs수행
            for j in range(m):
                if virusmap[i][j] == 2:
                    bfs(i,j,virusmap)

        for i in range(n): #벽을 세우고 bfs수행했으니까 안전지역 탐색
            for j in range(m):
                if virusmap[i][j] == 0:
                    count += 1
        result.append(count)
        count = 0

        graph[x1][y1] = 0 # 벽을 허물어줌
        graph[x2][y2] = 0
        graph[x3][y3] = 0
    else:
        continue

print(max(result))