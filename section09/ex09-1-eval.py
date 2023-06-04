'''
내장함수
    별도의 임포트 없이 어디서든 사용할 수 있는 함수
eval() 함수
    매개변수로 받은 expression(=식)을 문자열로 받아서
    실행하는 함수
'''
expr = input('계산식을 입력하세요 >>>')
result = eval(expr)

print(expr, '=', str(result))

