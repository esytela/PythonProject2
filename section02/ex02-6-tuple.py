'''
튜플 = 리스트랑 비슷함. 단일 변수에 여러 항목을 저장하는데 사용. 순서가 있고 변경할 수 없는 리스트. ()로 작성
'''

thistuple = ('피카츄', '라이츄', '파이리')
print(thistuple)

#튜플의 길이
print(len(thistuple))

#항목접근
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])

#튜플값 변경 방법
thistuple = ('피카츄', '라이츄', '파이리')
thiscast = list(thistuple) #list로 casting(형변환)
thiscast[1] = '잠만보'
thistuple = tuple(thiscast) #다시 튜플로 바꿈. 새로 만든 튜플이나 다름 없음
print(thistuple)

#튜플 압축 풀기
thistuple = ('피카츄', '라이츄', '파이리', '꼬부기')
(p1, p2, p3, p4) = thistuple
print(p1) #ctrl + d 줄복사, ctrl + y 줄삭제
print(p2)
print(p3)
print(p4)

#두개 튜플 조인
thistuple1 = ('피카츄', '라이츄', '파이리','꼬부기')
thistuple2 = ('버터플', '야도란', '피존투','또가스')
thistuple3 = thistuple1 + thistuple2
print(thistuple3)
