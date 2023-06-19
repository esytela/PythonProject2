import json

dict_list = [
    {
        'name':'james',
        'age':20,
        'spec':[175.5, 70.5]
    },
    {
         'name':'홍길동',
        'age':21,
        'spec':[168.6, 60.5]
    }
]
json_string= json.dumps(dict_list, indent=4, ensure_ascii=False)
# indent 들여쓰기, ensure_ascii=False 한글 읽기
with open('dictlist.json','w', encoding='UTF-8') as file:
    file.write(json_string)
print('dictlist.json 파일이 생성되었습니다')