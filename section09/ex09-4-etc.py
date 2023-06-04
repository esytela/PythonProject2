'''
#len() 데이터 길이
'''
text = 'Hello, World!'
print(len(text))

#abs() 절대값
result = abs(-10)
print(result)

#format()

#max() 최대값 반환
result = max(1,10)

#min() 죄소값 거듭제곱 함수
li = [1,2,3]
result = min(li)
print(result)

#pow() - 거듭제곱
result = pow(10,2)
print(result)

#sorted() - 정렬
my_li = [5,6,3,4,1,2,]
print(my_li)
result = sorted(my_li)
print(result)

#역정렬
result = sorted(my_li, reverse=True)
print(result)

#zip() 함수 - 같은 인덱스 번호끼리 튜플로 묶어 줍니다
names = ['james', 'emily', 'amanda']
scores = [60, 70, 80]
for student in zip(names, scores):
    print(student)

for name, score in zip(names, scores):
    print(f'{name}의 점수는 {score}점 입니다.')

