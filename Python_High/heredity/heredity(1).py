"""
상속
- 부모 클래스가 가진 속성과 메서드를 자식 클래스가 물려받는 것을 의미
- 상속을 통해 기존 클래스의 속성과 메서드를 물려받아 쓸 수 있음 => 코드 재사용
- 일반적으로 상위 분류 클래스로부터 상속
"""

# 클래스 상속의 예시
class Car: # 부모 클래스 생성
    def __init__(self, engine):
        self.engine = engine
        print("자동차 클래스의 생성자예요!")

class SportsCar(Car): # Car 클래스로부터 상속
    pass

my_sports_car = SportsCar("v8") # Car 클래스의 생성자 호출

print("이 자동차의 엔진: ", my_sports_car.engine)

""" 
메서드 오버라이딩
- 부모 클래스에서 물려받은 메서드를 자식 클래스에서 새로 정의하는 것을 의미
- 부모 클래스의 메서드와 동일한 이름의 메서드를 자식 클래스에 정의하여, 자식 클래스에 맞는 기능으로 변경 가능
- 메서드 오버라이딩을 통해 자식 클래스의 새로운 특성을 반영할 수 있음
"""

# 메서드 오버라이딩 예시
class SuperCar(Car): # Car 클래스로부터 상속
    def __init__(self, has_wing): # 생성자 메서드 오버라이딩
        self.has_wing = has_wing
        print("슈퍼카 클래스에서 생성자가 재정의되었어요!")

my_super_car = SuperCar(True)

print("이 자동차의 wing 보유 여부: ", my_super_car.has_wing)