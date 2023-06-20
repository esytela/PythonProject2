'''
상속 (inheritance)
    상위클래스 (부모클래스)가 가지고 있는 기능을
    그대로 물려받아 하위클래스 (자식클래스)에서 사용할 수 있다 (확장개념)

상속방법
class 상위클래스
    본문

class 하위클래스(상위클래스)
    본문
'''

class Coffee:
    def __init__(self, bean):
        self.bean = bean

    def coffee_info(self):
        print('원두: {}'.format(self.bean))

class Espresso(Coffee): #상속 방법. 자식(부모)
    def __init__(self, bean, water):
        super().__init__(bean) #super = 부모의 참조 키워드
        self.water = water #self는 자기 자신 참조

    def espresso_info(self):
        super().coffee_info() #이것도 부모꺼 따라함. 원두에 대한 코딩을 부모꺼를 상속받아 그대로 사용
        print('물: {}'.format(self.water))

coffee = Espresso('콜롬비아', 30)
coffee.espresso_info()

print(coffee.bean) #부모의 원두 정보
coffee.coffee_info() #coffee '.'을 누르면 어디 클래써거인지 알 수 있음