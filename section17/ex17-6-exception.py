import traceback

try:
    score = int(input('점수를 입력하세요 >>>'))
    if score <0 or score>100:
        raise Exception('점수는 0~100 사이 입니다.')
except Exception as e:
    print(e)
    traceback.print_exc()
#빨간색으로 에러가 뜸. 정확히 어디서 에러가 났는지 알 수 있음
else:
    if score >= 60:
        print('{}점은 합격입니다.'.format(score))
