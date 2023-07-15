def selection_sort(arr):
    for i in range(len(arr)):

        '''
        [5, 3, 4, 1, 2]
        i = 0
        '''

        min_idx = i

        for j in range(i + 1, len(arr)):

            '''
            [5, 3, 4, 1, 2]
            i = 0
            j = 1
            min_idx = 1

            i = 0
            j = 2
            min_idx = 
            '''

            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# 실행코드
arr = [5, 3, 4, 1, 2]
print(selection_sort(arr))
print(len(arr))

#https://evan-moon.github.io/2018/10/13/sort-algorithm/

