"""
private
- 클래스 내부에서만 호출 가능한 메서드
- 외부 사용자에게 필요없는 클래스 내부의 작업과 구조를 캡슐화하는 데 사용
- 클래스의 사용자가 클래스 내부의 복잡한 처리 과정을 이해하지 안하도 되게 함
"""

# print 메서드의 활용 예시
class Car:
    def __init__(self, fuel):
        self.__fuel = fuel

    def drive(self):
        if self.__check_fuel():
            print("주행해요")
        else:
            print("연료가 부족해요!")

    def __check_fuel(self): # private 메서드
        if self.__fuel < 1:
            return False
        self.__fuel -= 1
        return True
    
my_car = Car(1)
my_car.drive()
my_car.drive()
