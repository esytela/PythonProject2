'''
csv 모드 없이 그냥 읽는 법
'''

member_list = []
with open('회원명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        member = line.split(',')
        member[0] = member[0].strip('"')
        member[2] = member[2].strip('\n')
#strip = 제거
        member_list.append(member)

print(member_list)
