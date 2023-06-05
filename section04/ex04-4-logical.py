'''
논리 연산자
    관계 연사자와 함계 사용되는 연산자
    2개 이상의 항을 논리적으로 연결할 떄 사용
    ex) and, or, not
    and : 2개항 모두 True일때 True
    or : 2개항 어느 한쪽이 True이면 True
    not : 논리값을 반전 시킨다
'''
a = 10
b = 0
print('{} > 0 and {} > 0 : {}' .format(a,b,a>0 and b>0))
print('{} > 0 and {} > 0 : {}' .format(a,b,a>0 or b>0))

print('not {} : {}' .format(a, not a))
print('not {} : {}' .format(b, not b)) # 0 -> False로 인식

