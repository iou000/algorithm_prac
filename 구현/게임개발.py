direction = 0
#왼쪽으로 회전하는 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

def solution(N,M,c,map):
    x = c[0]
    y = c[1] # 초기 위치
    d = [[0] * M for _ in range(N)] #방문할 위치를 저장할 맵 초기화

    d[x][y] = 1#현재 좌표 방문 처리

    #이동할 방향 북 동 남 서 
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    def turn_left():
        global direction
        direction -= 1
        if direction == -1:
            direction = 3

    count = 1
    turn_time = 0
    while True:
        turn_left()
        #이동할 위치
        nx = x + dx[direction]
        ny = x + dy[direction]
        #이동할 위치에 가보지 않았거나 바다가 아니라면
        if d[nx][ny] == 0 and map[nx][ny] == 0:
            d[nx][ny] = 1 #방문처리
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue # 1단계로 돌아감
        #이동할 위치가 바다거나 가본 경우
        else:
            turn_time += 1
        #네 방향 모두 갈 수 없는 경우
        if turn_time == 4:
            # 뒤로 이동할 위치
            nx = x - dx[direction]
            ny = y - dy[direction]
            #뒤로 이동할 수 있다면
            if map[nx][ny] == 0:
                x = nx
                y = ny # 이동 (이동 후 1단계로 돌아감)
            #뒤로 이동할 곳이 바다라면
            else:
                break
            turn_time = 0

    return print(d)
N,M = 4,4
c = [1,1]
map = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
solution(N,M,c,map)
