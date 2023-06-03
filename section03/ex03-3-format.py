'''
format
    {}를 활용하여 데이터 종류에 상관없이 print문으로 표현이 가능
'''

print('올해는 {}년 입니다.'.format(2023))
print('올해는 {}년, 내년은 {}년입니다.' .format(2023,2024))
print('나는 {}을 공부합니다' .format('Python'))
print('나는 {}과 {}를 탑니다' .format('지하철', '버스'))

name = '홍길동'
age = '20'
print(f'제이름은 {name} 입니다. \n 나이는 {age} 입니다')
print('제이름은 {} 입니다. \n 나이는 {} 입니다'.format(name,age))


address = '''서울특별시 강남구
테헤란로 123
'''

print('주소: {addr}'.format(addr=address))

