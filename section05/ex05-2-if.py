age = int(input('나이를 인력하세요: '))
if age < 5:
    print('어린이들을 위한 놀이공원을 추천합니다!')
elif age >= 5 and age < 18:
    print('당신은 학생이시군요! 동아리에 가입해보는건 어떠세요?')
elif age >= 18 and age < 40:
    print('인생은 여행이죠! 다양한 여행지를 탐험해보세요')
elif age >=40 and age < 60:
    print('여가 시간을 활용하여 새로운 취미를 찾아보세요. '
          '그것이 인생의 힐링이 될 수도 있어요')
else:
    print('평화로운 여유로움이 필요')