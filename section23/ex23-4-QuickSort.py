'''
4. quick sort (퀵정렬)
    분할 정복 알고리즘의 일종, 기준점(pivot)을 설정하고
    pivot보다 작은 값은 왼쪽, 큰 값은 오른쪽으로 반할한 후
    각 부분 리스트에 대해 재귀적으로 퀵 정렬을 수행하는 알고리즘
'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left, right, equal = [], [], []
    for a in arr:
        if a < pivot:
            left.append(a)
        elif a > pivot:
            right.append(a)
        else:
            equal.append(a)

    return quick_sort(left) + equal + quick_sort(right)

#실행코드
arr = [6, 5, 3, 1, 8, 7, 2, 4]
print(quick_sort(arr))