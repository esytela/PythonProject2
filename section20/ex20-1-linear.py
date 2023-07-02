'''
자료구조
    데이터를 저장하고 조직화하는 방법론 (저장, 삭제)

선형리스트 (LinearList)
    간단한 자료구조 중 하나로, 데이터를 일렬로 나열한 것이다

'''

# 클래스 정리
class LinearList():
    def __init__(self):
        self.linear = []

#리스트에 데이터 추가 (빈공간 만들고 정보 넣고)
    def add_data(self, data):
        linear = self.linear
        linear.append(None) #빈 공간을 만든 후 여기에다가 데이터를 넣음
        lLen = len(linear)
        linear[lLen - 1] = data

# 데이터 삽입 (빈공간 새로 만들고 나머지는 밀고 데이터 넣고)
    def insert_data(self, position, data):
        linear = self.linear

        if position < 0  or position > len(linear): # len(linear) = 5. 0과 5사이에 값 추가 한다는 뜻
            print('데이터를 삽입할 범위를 벗어났습니다.')
            return

        linear.append(None)
        linearSize = len(linear)

        for i in range(linearSize - 1, position, -1): #5 (linearSize)부터 4까지 (positon=3)
            linear[i] = linear[i - 1] # linear 5가 4가 됨
            linear[i - 1] = None

        linear[position] = data

# 리스트 데이터 삭제 (삭제 -> 데이터 미뤄 -> 마지막에는 빈 공간 -> 빈 공간 삭제)
    def delete_data(self, position):
        linear = self.linear

        if position < 0 or position > len(linear):
            print('데이터를 삭제할 범위를 벗어났습니다.') # 범위에서 벗어나면 데이터 들어오는 것을 막음

        linear[position] = None
        linearSize = len(linear)

        for i in range(position + 1, linearSize):
            linear[i - 1] = linear[i]
            linear[i] = None

        del(linear[linearSize-1])

    def print_list(self):
        linear = self.linear
        for list in linear:
            print(list)

# 실행코드
linear = LinearList()
linear.add_data(3)
linear.add_data(5)
linear.add_data(4)
linear.add_data(2)
linear.add_data(6)

linear.insert_data(3,99)

linear.delete_data(2)

linear.print_list()
