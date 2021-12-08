# 파이썬 일부 라이브러리는 잘못 사용하면 수행시간이 비효율적으로 증가한다.
# 표준 라이브러리: 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리.
# 파이썬에서는 굉장히 많은 표준 라이브러리를 지원하지만 코딩테스트에서 반드시 알아야 할 라이브러리는 6가지정도.

# 내장함수 : print(), input(), sorted() 등 기본 내장 라이브러리
# itertools : 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리. 순열과 조합 라이브러리를 제공함.
# heapq: 힙(Heap) 기능을 제공하는 라이브러리. 우선순위 큐 기능을 구현하기 위해 사용됨.
# bisect : 이진탐색(Binary Search) 기능을 제공하는 라이브러리
# collections : 덱(deque), 카운터(Counter) 등 유용한 자료구조를 포함하고 있는 라이브러리.
# math : 필수 수학적 기능을 제공하는 라이브러리. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함.



# ---------- 내장함수 ----------
# 별도의 import 명령어 없이 바로 사용할 수 있음.

# sum()
# iterable 객체(반복 가능한 객체[리스트, 사전, 튜플 자료형 등])가 입력으로 주어졌을 때 모든 원소의 합을 반환
result = sum([1,2,3,4,5])
print(result)  #15

# min(), max()
# 파라미터가 2개 이상 들어왔을 때 가장 작은 값(min()), 가장 큰 값(max()) 반환
result = min(7,3,5,2)
print(result) #2
result = max(7,3,5,2)
print(result) #7

# eval()
# 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과 반환.
result = eval("(3 + 5) * 7")
print(result) #56

# sorted()
# iterable 객체가 들어왔을 때, 정렬된 결과를 반환. key 속성으로 정렬 기준 명시 가능, reverse 속성으로 내림차순 정렬 가능.
result = sorted([9,1,8,5,4]) #오름차순
print(result) #[1,4,5,8,9]
result = sorted([9,1,8,5,4], reverse=True) #내림차순
print(result) #[9,8,5,4,1]

# key 속성을 이용한 정렬 (튜플 두번째 원소 기준 내림차순)
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse=True)
print(result) # [('이순신', 75), ('아무개', 50), ('홍실동', 35)]

# sort() : iterable객체 내부 값이 정렬된 값으로 바뀜. 리스트명.sort()
# sorted() : 리스트 원본값은 그대로이고, 정렬된 값 반환. sorted(리스트명)



# ---------- itertools ----------
# 반복되는 데이터를 처리하는 기능을 포함하는 라이브러리.
# 코테에서 유용하게 사용할 수 있는 클래스는 permutations(순열), combinations(조합)

# ---permutations---
# iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열) 계산.
# permutations는 클래스이므로 객체 초기화 이후에는 리스트로 변환해 사용
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data,3)) #모든 순열 구하기 nPr => n! / (n-r)!
print(result) #[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# ---combinations---
# iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합) 계산.
# combinations는 클래스이므로 객체 초기화 이후에는 리스트로 변환해 사용
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data,2)) # 2개를 뽑는 모든 조합 구하기 nCr => n! / (n-r)!r! == nPr / r!
print(result) #[('A', 'B'), ('A', 'C'), ('B', 'C')]


# ---product(중복 순열)---
#iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 중복을 허용하여 계산.
# product는 클래스 이므로 객체 초기화 이후에는 리스트로 변환해 사용.
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) #2개를 뽑는 모든순열(중복 허용) nπr => n^r
print(result) #[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# ---combinations_with_replacement(중복 조합)---
# iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 중복을 허용하여 계산.
# combinations_with_replacement는 클래스이므로 객체 초기화 이후에는 리스트로 변환해 사용.
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2)) #2개를 뽑는 모든 조합 구하기(중복 허용) nHr => n+r-1Cr
print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]



# ---------- heapq ----------
# heapq는 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용됨.
# heapq 외에도 PriorityQueue 라이브러리를 사용할 수 있지만, 코테 환경에서는 보통 heapq가 더 빠르니까 heapq를 사용하도록 하자.
# 파이썬의 힙은 최소힙(min heap)으로 구성되어 있으므로 단순히 원소를 힙에 전부 넣었다 빼는 것만으로도 O(NlogN)에 오름차순 정렬이 완료됨.
# => 최소 힙 자료구조의 최상단 원소는 항상 '가장 작은'원소이기 때문.
# heapq.heappush() => 힙에 원소 삽입
# heapq.heappop() => 힙에서 원소를 꺼냄.

#힙 정렬을 heapq로 구현.
import heapq

def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# heapq 라이브러리를 이용해 최대 힙 구현(파이썬에서는 최대힙 제공x) ==> 내림차순 힙 정렬 구현
# 힙에 원소 삽입 전 잠시 부호를 반대로 바꾸었다 힙에서 원소를 꺼낸 뒤 다시 부호를 바꾸면 됨.
import heapq

def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result



# ---------- bisect ----------
# 파이썬에서 이진 탐색을 쉽게 구현할 수 있도록 제공하주는 라이브러리.
# '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용됨.
# bisect_left(), bisect_right() 함수가 가장 중요하게 사용됨. O(logN)

# bisect_left(a, x) : 정렬된 순서룰 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾음.
# bisect_right(a, x) : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 도른쪽 인덱스를 찾는 메서드

# 정렬된 리스트[1, 2, 4, 4, 8]에 데이터 4를 삽입할 인덱스 찾기
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a,x)) #2
print(bisect_right(a,x)) #4

# bisect_left(), bisect_right()는 '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구할 때 효과적으로 사용됨.
# 예를들어
# 정렬된 리스트에서 값이 [left_value, right_value]에 속하는 데이터의 개수를 반환하는 count_by_range(a, left_value, right_value)를 구현할 때
# (left_value <= x <= right_value인 원소의 개수를 O(logN)으로 빠르게 계산 가능).
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4)) #2
print(count_by_range(a, -1, 3)) #6



# ---------- collections ----------
# 유용한 자료구조를 제공하는 표준 라이브러리
# 코테에서는 deque, Counter 가 가장 유용하게 사용됨.

# --- deque ---
# 파이썬에서는 deque를 사용해 큐를 구현한다. (Queue 라이브러리가 있는데 일반적인 큐 자료구조를 구현하는 라이브러리는 아님)
# 리스트 자료형은 삽입, 삭제 등 다용한 기능을 제공하지만 append() or pop()으로 데이터를 추가or삭제 시
# '가장 뒤쪽'원소 기준이기 때문에 앞에 있는 원소를 처리할 때는 많은 시간이 소요될 수 있음. => 리스트 앞쪽 원소를 삽입or삭제시 O(N)
# deque에서는 인덱싱, 슬라이싱기능 사용 x.

# 스택, 큐 기능을 모두 포함한다고 볼 수 있어서 보통 스택or큐 자료구조의 대용으로 사용됨.
# 첫 번째 인덱스에 원소 삽입 : appendleft(x)
# 마지막 인덱스에 원소 삽입 : append(x)
# 첫 번째 원소 제거 : popleft()
# 마지막 원소 제거 : pop()

#리스트 [2,3,4]의 가장 앞, 뒤에 원소를 삽입
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(data) # deque([1,2,3,4,5])
print(list(data)) # [1,2,3,4,5] (리스트로 변환)

# --- Counter ---
# iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려줌.
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'greeen', 'blue', 'blue'])

#'blue'가 등장한 횟수 출력
print(counter['blue']) # 3
print(counter['green']) # 1

#사전 자료형으로 변환
print(dict(counter)) # {'red': 2, 'blue': 3, 'green': 1}



# ---------- math ----------
# 팩토리얼, 제곱근, 최대공약수(GCD) 등 자주 사용되는 수학적인 기능을 포함하는 라이브러리.
# 따라서 수학 계산을 요구하는 문제를 만났을 때 효과적으로 사용 가능.

# ---factorial(x) ---
import math
print(math.factorial(5)) # 120

#--- sqrt(x) ---
# x의 제곱근을 반환.
print(math.sqrt(7)) # 2.6457513110645907 (float)
print(math.sqrt(9)) # 3.0
print(list(map(int,[math.sqrt(9), math.sqrt(4)]))) #[3,2]

#--- gcd(a,b) ---
# a, b의 최대공약수
print(math.gcd(21,14)) #7

# 파이(pi)나 자연상수e 제공
print(math.pi) # 3.141592653589793 파이(pi)
print(math.e) # 2.718281828459045 자연상수 e