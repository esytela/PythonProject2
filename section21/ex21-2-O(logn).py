'''
O(logN)
    로그 시간 복잡도, 이진 탐색처럼 문제를 절반으로 나누어 해결하는 알고리즘

'''

def binary_search(arr, x):
    # 검색 범위의 시작점 설정
    low = 0
    # 검색 범위의 끝점 설정
    high = len(arr) - 1

    #시작점이 끝점보다 작거나 같을 때까지 반복
    while low <= high:
        mid = (low + high) // 2 #검색범위 중간 값

        # 1, 3, 5, 7, 8, 9, 10, 11, 21
        if arr[mid] < x: # 중간점의 값이 찾고자 하는 값보다 작은 경우
            low = mid + 1 # 검색 범위의 끝점을 중간점 다음 인덱스로 설정
        elif arr[mid] > x: # 중간점 값이 찾고자 하는 값보다 큰 경우
            high = mid - 1 # 검색 범위의 끝점을 중간점 이전 인덱스로 설정
        else:
            return mid

    return -1 # 찾고자 하는 값이 없는 경우 -1 반환

# 실행코드
arr = [1, 10, 5, 7, 8, 9, 3, 11, 21]
arr = sorted(arr)
print(arr)
print(binary_search(arr, 5))

