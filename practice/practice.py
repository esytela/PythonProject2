name = 'estela'
print(name)

x, y, z = '피카츄', '라이츄', '파이리'
print(x, y, z)

x = y =z = '꼬부기'
print(x)
print(y)
print(z)

'''
variables
    str = 텍스트
    int, float, comple = 숫자
    list, tuple, range = 시퀀스   
    dict = 매핑?
    set = 세트
    bool = 논리
    bytes, bytearray
    none
'''
x = 'estela'
print(type(x))
x = 12
print(type(x))
x = 12.5
print(type(x))

x = ['a','b','c']
print(type(x))
x = ('a','b','c')
print(type(x))

x = range(3)
print(type(x))

x = {"name" : 'estela', 'place':'korea'}
print(type(x))

x = {'a','b','c'}
print(type(x))

x = True
y = False
print(type(x))
print(type(y))

x = None
print(type(x))

num1 = 20
num2 = 10
print(num1 + num2)
print(str(num1),str(num2))

num1 = '20'
num2 = '10'
print(num1,num2)

print(num1 + num2)


print('hello' == "hello")
print(20 == 10)

#indexing
'''
h  e  l  l  o
1  2  3  4  5
-5 -4 -3 -2 -1
'''
str= 'estela'
print(str[-6])
print(str[1])
print(str[-4])
print('ela')

str = 'estela'
print(str[1:3])
print(str[-6:-2])
print(str[2:])
print(str[:4])
print(str.upper())
print(str.lower())
print(str.replace("a","o"))

'''list'''

list = ['a','b','c','d']
print(list)
print(list[1])
list1 = ['a','b','c','d']
list2 = [1, 2, 3, 4, 5]
list3 = [True, False, True]
list4 = ['abc', 20, True]

list1[1:3] = 'z','y'
print(list1)

list2[1:3] = '4'
print(list2)

list.append('e')
print(list)

list = ['a','b','c','d']
list.remove('a')
print(list)

list.pop(2)
print(list)

list.pop()
print(list)

list.clear()
print(list)

list = ['a','b','c','d']
list.extend(['e','f'])
print(list)

print('빨리와')