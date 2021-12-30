#입력 받기
n,l = map(int,input().split())

#지도 초기화
road = []
for i in range(n):
    road.append(list(map(int, input().split())))

#행,열 바꾼 지도
road2 = list(map(list, zip(*road)))

def road_check(n, l, road):
    runway = [0] * n

    for i in range(n-1):
        #현재칸 숫자가 다음칸 숫자와 같으면 pass
        if road[i] == road[i+1]:
            continue
        #현재 숫자와 다음 숫자의 차이가 1보다 크면 길없음
        elif abs(road[i] - road[i+1]) > 1:
            return False
        elif road[i] - road[i+1] == 1: # 다음 숫자가 1작은 경우
            if i + l > n-1: #경사로가 밖으로 빠져나갈시 false
                return False
            for j in range(l): #앞의 숫자들이 경사로의 길이만큼 같은지 확인 다르면 false
                if road[i+1] != road[i+1+j]: 
                    return False
            for j in range(l): #확인이 돼서 위에 for문을 통과하면 경사로를 ckeck해줌
                runway[i+1+j] = 1
        elif road[i] - road[i+1] == -1: # 다음 숫자가 1큰 경우
            if i + 1 - l < 0: # 경사로가 밖으로 빠져나갈시 false
                return False
            for j in range(l): #뒤의 숫자들이 경사로의 길이만큼 다음 숫자보다 1 작은 숫자인지 확인
                if runway[i-j] == 1: #경사로가 이미 존재하면 false
                    return False
                if road[i-j] != road[i]: # 뒤의 숫자들이 경사로의 길이만큼 같은지 확인 다르면 false
                    return False
    return True

count = 0
for i in range(n):
    if road_check(n, l, road[i]) == True:
        count += 1

for i in range(n):
    if road_check(n,l,road2[i]) == True:
        count += 1

print(count)