# 이진탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있다.
# => 데티어가 정렬되어 있어야만 할 수 있지만 매우 빠름. O(logN)
# 탐색범위를 절반씩 좁혀가며 데이터를 탐색.

# 변수 3개 사용(시작점, 끝점, 중간점).
# => 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾음.


#이진탐색 구현(재귀)
def binary_search(array, start, end, target):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, start, mid-1, target)
    elif array[mid] < target:
        return binary_search(array, mid+1, end, target)

#이진탐색 구현(반복문)
def binary_search_while(array, start, end, target):
    while start <= end:       
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None


# ------------------실행------------------
array = ['1','2','3','4','5','6','7','8','9','10']
print('배열 : ' + str(array))

print('찾고자하는 원소 입력')
n = input()

print('원소의 위치 찾기 O(logN) : '+ str(binary_search_while(array, 0, len(array)-1, n)+1))