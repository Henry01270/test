"""
클래스 메서드
- 인스턴스 각각의 상태가 아닌 클래스 전체의 상태를 변경하는 메서드
- 클래스 레벨에서 작동하며 모든 인스턴스에 영향을 미침
- def 키워드 윗줄에 '@classmethod'라는 데코레이터를 작성하여 클래스 메서드임을 명시
- 클래스 메서드는 첫 번쨰 매개변수로 클래스 자체를 가리킬 수 있는 cls 매개변수를 가짐
    1. 'cls.속성명'과 같이 클래스의 속성에 접근할 수 있음
    2. cls 대신 다른 변수 이름을 사용할 수 있지만, cls가 일반적
- 클래스 외부에서는 '클래스명.메서드명()을 통해 클래스 메서드를 호출
"""

# 클래스 메서드를 포함하는 클래스
class Car:
    # 클래스 속성
    num_cars_produced = 0

    def __init__(self, color, engine):
        self.color = color
        self.engine = engine

        # 인스턴스 생성 시마다 클래스 속성 업데이트
        Car.num_cars_produced += 1

    # 클래스 메서드를 의미하는 데코레이터
    @classmethod
    # 클래스 메서드의 첫 번째 매개변수는 클래스 자체를 가리키는 매개변수 cls
    def print_num_cars(cls):
        print(f"자동차는 현재 {cls.num_cars_produced}대 입니다.")

# 클래스 메서드 호출
Car.print_num_cars()

# 인스턴스 생성 시 생성자가 호출되며 클래스 속성 업데이트
my_first_car = Car("하얀색", "v8")

# 클래스 메서드 호출
Car.print_num_cars()

"""
데코레이터(decorator)
- 데코레이터는 함수를 인자로 전달 받아 추가 기능을 수행하는 방법
- 데코레이터를 사용하면 기존 함수를 수정하지 않으면서 수행 결과를 변경하거나 보강할 수 있음
"""

# 데코레이터로 함수의 기능을 추가한 예시
def my_decorator(func):
    def wrapper():
        print("함수의 전처리 코드")
        func()
        print("함수의 후처리 코드")

    return wrapper

@my_decorator
def my_function():
    print("함수 실행 중")

# 데코레이터에 의해 my_decorator() 함수로 전달
my_function()
"""
- '@classmethod'는 데코레이터의 한 종류로, 메서드를 클래스 메서드로 지정하여 첫 번쨰 매개변수로 'cls'를 가짐
- 이를 통해 클래스 자체에 대한 작업을 수행
"""