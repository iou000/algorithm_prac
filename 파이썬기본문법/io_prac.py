# 파이썬에서 데이터를 입력받을 때는 input()을 이용함.
# input()은 한 줄의 문자열을 입력 받도록 해줌.

# 입력받은 문자열을 띄어쓰기로 구부내 각각 정수형 데이터로 저장하는 코드.
# 정말 많이 사용됨.
#  => list(map(int, input().split()))

# 공백, 줄바꿈을 기준으로 데이터를 구분하는 문제가 매우 많음.
# 구분자가 줄바꿈이라면  => int(input())을 여러번 사용.
# 구분자가 공백이라면 => list(map(int, input().split())) 사용.

#데이터 개수 입력 
n = int(input()) #5
#각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split())) #65 90 75 34 99

data.sort(reverse=True)
print(data) # [99,90,75,65,34]


# 입력 개수가 많은 경우
# sys.stdin.readline() 함수 이용
# input()과 같이 한 줄씩 입력받기 위해 사용함.
# readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거하려면 rstrip()함수를 사용해야 함.
# 관행적으로 외워서 사용 ㄱㄱ
import sys
data = sys.stdin.readline().rstrip()
print(data) # Hello World

# 출력할 때는 print() 사용
# 각 변수를 콤마(,)로 구분해 매개변수로 넣을 수 있음. 이 경우 각 변수가 띄어쓰기로 구분되어 출력됨.

# 문자열과 수를 함께 출력해야 하는 경우
# 문자열 자료형 끼리만 더하기 연산이 가능해서 str() 함수를 이용해 바꿔줘야함.
answer = 7
print("정답은 " + str(answer) + "입니다.") # 정답은 7 입니다
print("정답은", str(answer), "입니다.") # 정답은 7 입니다

# f-string
# 문자열 앞에 접두사 'f'를 붙여서 사용, 중괄호({})안에 변수를 넣어 형변환 없이도 문자열과 정수를 함께 넣을 수 있음.
print(f"정답은 {answer}입니다.")