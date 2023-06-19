'''
JSON (Javascript Object Notation)
    데이터를 키와 값의 쌍을 중괄호({})로 묶어 표현하는 형식
    - 딕셔너리와 비슷하다
    - 구조 { K : V }
'''

import json

dict_list = [
    {
        'name' : 'james',
        'age':20,
        'spec': [175.7, 70.5]
    },
    {
        'name':'alice',
        'age':21,
        'spec':[168.5, 60.5]
    }
] #dict 안에 두개의 값
print(dict_list)

json_string = json.dumps(dict_list)

with open('dictlist.json', 'w') as file:
    file.write(json_string)
print('dictlist.json 파일이 생성되어습니다')
