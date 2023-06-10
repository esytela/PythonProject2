'''
모듈 사용법
    from 모듈명 import 함수 #함수가 한정적일때
    from 모듈명 import 함수1, 함수 2 #여러 함수
    from 모듈명 import * #별표는 전체 사용한다는 뜻
'''

from converter import kilometer_to_miles

miles = kilometer_to_miles(150)
print('150km = {}miles'.format(miles))