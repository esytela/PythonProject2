'''
mutable = 메모리 값을 변경 가능 객체
 list, set, dict
 주소값이 안 바뀜
'''
me = [1, 2, 3]
print(me)
print(id(me)) #2518019116800 주소값
#주소값을 통해서 리스트에 접근
me.append(4) #4의 값이 추가가 됨. 그러나 주소값은 동일
print(me)
print(id(me))

'''
immutable = 메모리 값 변경 불가
    int, float, str, tuple
    값이 바뀌면 주소값도 바뀜
'''

me = 10
print(me)
print(id(me)) #140723697214536

me += 1 #me는 me+1이 된다. 그럼 10+1이 되는 것이다
print(me)
print(id(me)) #140723697214568 주소값이 다름.
#이전 value를 수정하는 것이 아닌 메모리에서 새로 만드는 것

