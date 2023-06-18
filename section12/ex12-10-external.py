'''
패키지
    모듈 상위 개념
    모듈의 집합을 의미한다

라이브러리 - 패키지 집합

pip - 패키지 관리자 도구
    PYPL(Python Pacakge Index)에서 패키지를 다운로드
    수많은 오픈소스가 저장되어 있는 중앙 저장소

패키지 설치
    console
    C :\> - window 기준
        C:\> pip install package명
        $ - mac기준

패키지 삭제
    C :\> pip uninstall package명
'''

# 행렬 연산 관련 pacakge
import numpy as np
print(np.sum([1, 2, 3, 4, 5]))

a = np.array([1,2,3])
b = np.array([4,5,6])

#각 요소 더하기
c = a + b
print(c)
c = np.add(a,b)
print(c)

#각 요소 뺴기
c = a - b
c = np.subtract(a, b)
print(c)

#각요소 곱하기
c = a * b
c = np.multiply(a,b)
print(c)

# 각 요소 나누기
c = a / b
c = np.divide(a,b)
print(c)