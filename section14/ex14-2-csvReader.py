'''
CSV(comma-separated values)
    필드를 쉼표(,)로 구분한 텍스트 데이터 파일
'''
student_list= []
with open('학생명단.csv', 'rt', encoding='UTF-8') as file:
    #r/rt = read text 단위로
    #rb = read bytes 단위로
    file.readline( )
    while True:
        line = file.readline()
        if not line:
            break

        student = line.split(' , ')
        student_list.append(student)
print(student_list)


















