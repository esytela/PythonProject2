'''
해시테이블 (Hash Table)
-> 키와 값을 저장하는 데이터 구조
    요소를 빠르고 효율적인 검색, 삽입, 삭제를 허용한다.
    해시 함수는 키를 입력으로 받아 값을 저장하거나 검색할 수 있는
    배열 인덱스를 반환한다

키 -> hash function으로 코드 받음
'''

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * self.size #빈값을 * 4
                #10개의 리스트가 생긴다고 볼 수 있다

    def has_function(self, key):
        return hash(key) % self.size #0~9까지의 값이 나옴

    def insert(self, key, value):
        #이름 = key, 전화번호 = value
        hash_index = self.has_function(key) #인덱스 값 받음

        if self.hash_table[hash_index] is None:
            self.hash_table[hash_index] = []
        self.hash_table[hash_index].append((key, value)) #key, value의 튜플 넣어줌

    def search(self, key):
        hash_index = self.has_function(key)
        bucket = self.hash_table[hash_index]
        if bucket is None:
            return None
        for k, v in bucket:
            if k == key:
                return v
        return None

# 실행코드
print(hash('KoreaIT') % 10) #매번 실행 할때마다 hash 값이 다르지만 실행중에는 값이 안 바뀜
hash_table = HashTable(10) #hash_table 객체 생성. 사이즈는 10
hash_table.insert('John Doe', '555-555-5555')
hash_table.insert('Jane Doe', '555-555-5556')
hash_table.insert('Jim Doe', '555-555-5557')
hash_table.insert('KoreaIT', '555-555-5558')

#키 값으로 전화번호 가져옴
print(hash_table.search('John Doe'))
print(hash_table.search('Jane Doe'))
print(hash_table.search('Jim Doe'))
print(hash_table.search('KoreaIT'))