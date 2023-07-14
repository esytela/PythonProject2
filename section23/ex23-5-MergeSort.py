'''
병합정렬(Merge Sort)
    분할정복 알고리즘의 일종으로, 리스트를 절반으로 나눈 후
    각각을 재귀적으로 합병하고 정렬하고, 다시 합치면서 정렬하는 알고리즘
'''


def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # 길이가 1이면 정렬할 필요가 없음

    mid = len(arr) // 2  # 4

    left = merge_sort(arr[:mid])  # 리스트를 미드까지 짜르는 것. 미드 전
    right = merge_sort(arr[mid:])  # 미드 후
    '''
  [5, 2, 8, 6, 1, 9, 3, 7]
    mid = 4
    left = 5, 2, 8, 6
    right = 1, 9, 3, 7

    left = 5, 2 right = 8, 6 -> left = 5 right = 2 -> 이 상태에서 merge(left,right)
    left = 1, 9 right = 3, 7 <- len = 1이 될때까지 이 과정 반복
    '''

    return merge(left, right)


def merge(left, right):
    result = []

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


arr = [5, 2, 8, 6, 1, 9, 3, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)
