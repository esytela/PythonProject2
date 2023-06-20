'''
서버 요청 - request
서버 응답 - response

http 응답(response)코드
    200번대 응답: 성공 (success)
    300번대 응답: 리다이렉션 (redirection)
    400번대 응답: 클라이언트 에러 (Client error)
        ex) 404 찾을 수 없는 페이지 (주소 잘못 입력)
            403 권한 문제
    500번대 응답 : 서버 에러 (Server error)
        (개발자 코드 에러 발생 했을 경우)
'''
import requests

url = 'https://www.youtube.com/'
response=requests.get(url)
print('응답 코드: {}'.format(response.status_code))

