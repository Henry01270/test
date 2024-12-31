"""
클래스 속성
- 해당 클래스에 속하는 모든 인스턴스가 공유하는 변수를 말함
    1. 모든 인스턴스에 대한 공통적인 정보를 저장하고 관리하는데 사용
    2. 인스턴스마다 다른 값을 가질 수 있는 인스턴스 속성과는 다름
- 'self'를 사용하지 않고, '클래스명.속성명'을 사용
"""

# 클래스 속성 업데이트와 출력
class Car:
    # 클래스 속성
    num_cars_produced = 0

    def __init__(self, color, engine):
        self.color = color
        self.engine = engine

        # 인스턴스 생성 시마다 클래스 속성 업데이트
        Car.num_cars_produced += 1

# 클래스 속성은 인스턴스를 생성하지 않아도 접근 가능
print(Car.num_cars_produced) # 0

# 인스턴스 생성 시 생성자가 호출되며 클래스 속성 업데이트
my_first_car = Car("파란색", "v12")
print(Car.num_cars_produced)

my_second_car = Car("하얀색", "v8")
print(Car.num_cars_produced)

my_third_car = Car("빨간색", "v10")
print(Car.num_cars_produced)