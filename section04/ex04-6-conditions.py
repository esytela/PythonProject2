'''
조건 연산자 (삼항 연산자)
    조건식 결과에 따라 참 또는 거짓의 결과를 반환 한다
    참 if 조건식 else 거짓
'''
a = 20
b = 100
result = (a-b) if (a>=b) else (b-a) #한줄로 코드 써야할떄 씀
print(f'{a}과 {b}의 차이는 {result}입니다')