"""
getter와 setter

getter
- private 속성의 값을 외부로 전달하는 기능을 하는 메서드
- private 속성의 값을 확인

setter
- private 속성의 값을 내부에서 변경하는 기능을 하는 메서드
- private 속성을 조건에 맞도록 안전하게 변경
- 속성의 값을 변경하기 전 변경할 값이 특정 조건을 충족시키는지 확인 가능
"""

# getter와 setter의 활용 예시

class Car:
    def __init__(self, color, engine, owner):
        self.color = color
        self.engine = engine
        self.__owner = owner

    def get_owner(self): # getter
        return self.__owner
    
    def set_owner(self, new_owner): # setter
        if "@abc.com" in new_owner:
            self.__owner = new_owner
        else:
            print("자동차를 소유 가능한 소속이 아닙니다.")

my_car = Car("파란색", "v6", "justin@abc.com")
print(my_car.get_owner())

my_car.set_owner("john@abc.com") # 조건에 맞는 업데이트
print(my_car.get_owner())

my_car.set_owner("mike@cv.com") # 조건에 맞지 않는 업데이트 시도
print(my_car.get_owner())