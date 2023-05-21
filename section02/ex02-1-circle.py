'''

개요: 반지름을 전달하면 원의 넓이를 반환하는 get_area()함수
ctrl + / = #

'''

# math 모들 포함 (다른 사람이 만들어놓은 파이썬 코드를 사용하겠다는 뜻이다. math라는 module/library를 사용한다는 뜻)
# (기본적으로 파이썬에서 제공)
import math

# get_area() 함수정의
# 함수 = 코드들을 모아둠. 실행된 것이 아닌 정의만 한 것
def get_area(radius):
    """반지름을 입력 받아서 원의 넓이를 반환하는 get_area() 함수"""
    area = math.pi * math.pow(radius, 2)
    #pow = 반지름의 제곱. =는 같다는 뜻이 아니라 대입을 한다는 뜻이다.
    return area
# return = 계산된 결과를 돌려주겠다는 뜻

#여기부터 프로그램 실행 (실행코드)
radius = 1.5

# get_area() 함수 호출 결과를 area 변수에 저장
area = get_area(radius)
print(area)
print(get_area.__doc__) # Docstring
#마우스 올리면 해당 변수가 어떤 의미인지 볼 수 있음 (docstring)어떤 목족의 함수인지 알려주는 의미
