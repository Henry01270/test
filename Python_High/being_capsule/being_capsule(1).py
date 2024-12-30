"""
캡슐화
- 클래스의 속성과 동작을 하나의 단위로 감싸는 것을 의미
- 클래스 내의 중요한 데이터에 대한 외부 접근을 막아 클래스의 안정성을 높일 수 있음
- 클래스의 내부 구현을 알 필요 없이, 외부에서 필요한 정보와 동작만을 간편하게 이용

pubic 속성과 메서드
- 클래스 내부, 외부 모두 접근 가능
- 클래스의 속성과 메서드는 기본적으로 pubic

private 속성과 메서드
- 클래스 내부에서만 접근 가능하며, 외부에서는 접근불가
- 정의하기 위해서는 언더스코어(_)를 두개를 붙여서 정의
- 중요한 데이터 private로 설정하여 캡슐화로 보호
"""

class Car:
    def __init__(self, color, engine, owner):
        # pubic 속성
        self.color = color
        self.engine = engine
        self.engine_started = False

        # private 속성
        self.__owner = owner

# 인스턴스 생성
my_car = Car("파란색", "v6", "justin@abc.com")

# 외부에서 public 속성에 접근 가능
print("색상: ", my_car.color)
print("엔진: ", my_car.engine)
print("엔진 가동 여부: ", my_car.engine_started)

# 외부에서 private 속성에 접근 불가능
print("소유자: ", my_car.__owner)




""" public, private, protected 속성 """

class Person:
    def __init__(self, name, id, password):
        # public 속성 name
        self.name = name

        # protected 속성 _id
        self._id = id

        # private 속성 __password
        self.__password = password

person = Person("김코딩", "codingkim", "secret123")

# public 속성 name: 외부에서 접근 가능
print(person.name)

# protected 속성 _id: 외부에서 접근 가능하나 권장되지 않음
print(person._id)

# private 속성 __password: 외부에서 접근 불가능
print(person.__password)