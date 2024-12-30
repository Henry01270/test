"""
super() 함수
- 자식 클래스에서 부모 클래스의 원래 메서드를 호출하기 위해 super() 함수를 활용
- 생성자 역시 자식 클래스에서 super() 함수를 사용하여 부모 클래스의 생성자를 호출
- 이를 통해 부모 클래스의 인스턴스 속성을 초기화하고, 자식 클래스의 특성을 추가
- super() 함수는 메서드 오버라이딩과 함께 사용하여 부모 클래스의 기능을 확장하거나 수정
"""
"""
# super() 함수 호출 예시
class ChildClass(parentClass): # 부모 클래스로부터 상속
    def ChildMethod(self): # 자식 클래스의 메서드
        super().ParentMethod() # 부모 클래스의 메서드 호출
"""
# super() 함수를 이용한 부모 클래스의 메서드 호출
class Car:
    def __init__(self, engine):
        self.engine = engine
        self.engine_started = False
        print("자동차 클래스의 생성자예요!")

    def start_engine(self):
        self.engine_started = True
        print("엔진을 켰어요.")

# Car 클래스를 상속받는 SportsCar 클래스
class SportsCar(Car):
    # 메서드 오버라이딩
    def __init__(self, engine, has_wing):
        # 부모 클래스의 생성자를 호출하여 engine 속성 초기화
        super().__init__(engine)
        self.has_wing = has_wing
        print("스포츠카 클래스의 생성자예요!")
    
    # 메서드 오버라이딩
    def start_engine(self):
        print("부르릉!")

        # 부모 클래스의 메서드를 호출하여 engine_started 속성 업데이트
        super().start_engine()

my_sports_car = SportsCar("v8", True)
my_sports_car.start_engine()