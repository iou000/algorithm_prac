input = 'c2'

# 입력으로 들어온 문자를 숫자로 바꾸고싶다 : int(ord())를 사용하자


def solution(input):
    answer = 0
    
    #행
    row = int(input[1])
    #열
    col = int(ord(input[0]) - int(ord('a'))+1)

    #말의 이동방향 8가지 (열 이동, 행 이동)
    steps = [(-2,-1),(-2,1),(2,-1),(2,1),(1,-2),(-1,-2),(1,2),(-1,2)]
    
    for step in steps:
        #말 이동시키기
        nextrow = row + step[0]
        nextcol = col + step[1]

        #이동한 말이 8x8 평면안에 있다면
        if nextrow >= 1 and nextrow <=8 and nextcol >= 1 and nextcol <=8:
            answer +=1

    return answer
print(solution(input))