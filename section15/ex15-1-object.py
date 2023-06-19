'''
클래스 (class)
    클래스는 객체를 생성하기 위한 탬플릿
    객체를 만드는 설계도, like 와플 기계
    객체화 (인스턴스화) - 메모리에 올리는 것

객체 (object)
    현실 세계에 존재하는 물리적, 추상적 개념을 프로그램으로 표현한 것
    예) 물리적 - 자동차, 컴퓨터, 모니터 등.
        추상적  - 주문 정보, 배송 --> 문서화 할 수 있는 것들

객체 구성
    초기화용 - 생성자
    속성 - 변수
    기능 - 메서드(method)

개비지 콜렉터 (Garbage Collector)
'''

class Computer:
    def set_spec(self, cpu, ram, vga, ssd):
    #self = 본인 객체를 창조하는 (즉, computer에 입력되는 값은 computer self.cpu, self.ram에 들어간다는 뜻)
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print('CPU = {}'.format(self.cpu))
        print('RAM = {}'.format(self.ram))
        print('VGA = {}'.format(self.vga))
        print('SSD = {}'.format(self.ssd))

desktop = Computer() #Computer 객체 생성
desktop.set_spec('i7', '16GB', 'GTX3060', '512GB')
desktop.hardware_info()
print()
desktop.cpu = 'i9'
desktop.hardware_info()
print()

print('macbook')
macbook = Computer()
macbook.set_spec('M2', '16GB', 'M2', '512GB')
macbook.hardware_info()












