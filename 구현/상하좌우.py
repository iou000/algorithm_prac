# 입력
# 5
# R R R U D D

N = 5
step = ['R', 'R', 'R', 'U', 'D', 'D', 'L', 'L']


# ----------------내 풀이----------------
def lrud1(n, plans):
    x, y = 1, 1
    
    for plan in plans:
        if plan == 'L' and 1 < y:
            y -= 1
        elif plan == 'R' and y < N:
            y += 1
        elif plan == 'U' and 1 < x:
            x -= 1
        elif plan == 'D' and x < N:
            x += 1
        else:
            continue

    return [x,y];
# ---------------------------------------

# ---------------문제 해설----------------
def solution(n, plans):

    x,y  = 1,1
    #L, R, U, D에 따른 이동방향 (좌우상하)
    dx = [0,0,-1,1] #상하
    dy = [-1,1,0,0] # 좌우
    move_type = ['L', 'R', 'U', 'D']

    #이동 계획(plans)을 하나씩 확인
    for plan in plans:
        #이동 후 좌표 구하기
        for i in range(len(move_type)):
            if plan == move_type[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        #공간을 벗어나는 경우 무시
        if nx<1 or ny<1 or nx>n or ny>n:
            continue
        #이동 수행
        x,y = nx, ny

    return [x,y]

# ---------------------------------------


print(lrud1(N,step))
print(solution(N, step))
