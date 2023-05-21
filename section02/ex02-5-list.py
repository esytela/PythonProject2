'''
list = 단일 변수에 여러 항목을 저장하는데 사용
순서가 지정되고 변경 가능하며 중복값 허용
다양한 데이터 유형이 포함될 수 있다
'''

thislist = ['피카츄', '라이츄', '꼬부기']
print(thislist) #리스트에도 인덱스 번호가 있음
print(thislist[0]) #리스트에서 0번째 항목을 가져옴

#list 길이
print(len(thislist)) #len() 함수 리스트 길이. 리스트가 몇개의 요소를 가지고 있는지 길이를 알 수 있음

#list 데이터 유형
list1 = ['피카츄', '라이츄', '파이리']
list2 = [1, 2, 3, 4, 5]
list3 = [True, False, True]
List4 = ['abc', 34, False, 56]

#항목접근
thislist = ['피카츄', '라이츄', '파이리']
print(thislist[1])

#변경
thislist[1] = '잠만보'
print(thislist)

#항목 변경 2개
thislist = ['피카츄', '라이츄', '파이리','꼬부기', '버터플', '아도란']
thislist[1:3] = ['울먹이', '메타몽'] #이러면 라이츄와 파이리를 울먹이와 메타몽으로 바꿈
print(thislist)

#두번째 세번째 값을 하나의 값으로 변경
thislist = ['피카츄', '라이츄', '파이리','꼬부기', '버터플', '아도란']
thislist[1:3] = ['잠만보']
print(thislist)

#항목 추가
thislist = ["피카츄", '라이츄', '파이리']
thislist.append("꼬부기")
print(thislist)

#항목 추가 - 인덱스번호로 추가
thislist = ['피카츄', '라이츄', '파이리']
thislist.insert(1, '잠만보')
print(thislist)

#항목 값으로 제거
thislist = ['피카츄', '라이츄', '파이리']
thislist.remove('라이츄')
print(thislist)

#항목을 지정된 인덱스로 제거
thislist = ['피카츄','라이츄', '파이리']
thislist.pop(2)
print(thislist)

#마지막 값 제거
thislist = ['꼬부기', '버터플', '라도란', '피존투']
thislist.pop()
print(thislist)

#목록삭제
thislist = ['피카츄','라이츄', '파이리']
thislist.clear()
print(thislist)

#확장
thislist = ['피카츄','라이츄', '파이리']
thislist.extend(['버터플', '잠만보']) #다른 리스트 추가
print(thislist)

#객체 삭제
del thislist
print(thislist) #에러가 떠야함 'thislist'is not defined이라 뜸.