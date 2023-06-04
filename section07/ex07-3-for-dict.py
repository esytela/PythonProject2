'''
for문과 dict
'''

eng_dict = {
    'sun':'태양',
    'moon':'달',
    'star':'별',
    'space':'우주'
}

for word in eng_dict:
    print(f'{word}의 뜻: {eng_dict.get(word)}')

