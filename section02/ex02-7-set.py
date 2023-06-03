'''
set
    순서가 없음
    인덱싱 되지 않는 컬렉션
    중복값 없음
'''

thisset = {'피카츄', '라이츄', '파이리'}
print(thisset)
#실행 할 때마다 순서가 바뀐다

#항복 가져오기
#this set에 있는 값을 x에 대입 (이것은 반복문이다)
for x in thisset: #thisset의 길이 만큼 반복
    print(x)

#값이 있는지 확인
thisset = {"피카츄", '잠만보', '야도란'}
print("피카츄" in thisset) #True
print("꼬부기" in thisset) #False

#항복 추가하기
thisset.add('꼬부기')
print(thisset)

#다른 set 항목 추가
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {'꼬부기', "잠만보", "뮤츠"}
thisset1.update(thisset2)
print(thisset1)

#항목제거
thisset = {'피카츄', '라이츄', '파이리'}
thisset.remove('피카츄')
print(thisset)

#thisset.remove('피카츄')
#print(thisset) #없는 것을 remove 하면 error라고 뜸

thisset = {'피카츄', '라이츄', '파이리'}
thisset.discard('피카츄')
print(thisset)
thisset.discard('피카츄')
print(thisset) #없는 항목 삭제시 에러 ㄴㄴ

thisset.pop() #랜덤으로 하나씩 제거
#원래 pop은 마지막꺼를 제거하지만 set은 순서가 없기에 랜덤으로 제거
print(thisset)

#비우기
thisset.clear()
print(thisset)

#