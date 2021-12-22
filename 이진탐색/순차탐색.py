#순차탐색 시간복잡도 : O(N)
def sequential_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i + 1



print("문자열을 띄어쓰기로 구분하여 입력하세요.")
array = input().split()

print("찾을 문자열을 입력하세요.")
target = input()

print('찾은 문자열의 번호 : ' + str(sequential_search(array, target)))