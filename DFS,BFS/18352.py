from collections import deque

#도시 개수, 도로 개수, 거리 정보, 출발 번호
n, m, k, x = map(int, input().split())

graph = [[] * n for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

#출발점에서 각 도시까지의 거리를 저장하는 리스트
distance = [-1] * (n+1)
distance[x] = 0 # 출발도시는 0

def bfs(graph,x):
    
    queue = deque()
    queue.append(x)

    while queue: # 큐가 빌 때 까지
        current_node = queue.popleft()

        for next_node in graph[current_node]:
            if distance[next_node] == -1: #다음 노드가 방문하지 않은 노드라면
                distance[next_node] = distance[current_node] + 1 #다음 노드 까지의 거리는 현재 노드 + 1
                queue.append(next_node)

bfs(graph,x)

exist = False
for i in range(len(distance)):
    if distance[i] == k:
        exist = True
        print(i)
if exist == False:
    print(-1)
