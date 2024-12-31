"""
mutable 객체 업데이트시 주의점
- 리스트 딕셔너리와 같이 최초 생성 이후에 수정할 수 있는 데이터 타입을 가진 객체는 mutable 객체
- mutable 객체를 생성자의 인자로 전달한 경우, 클래스 외부에서 값을 업데이트하면 클래스 내부에서도 수정 사항이 반영됨

# mutable 객체의 업데이트와 반영 확인
class Cafe:
    def __init__(self, menu):
        self.menu = menu

# 객체의 초기 상태
menu = {"아메리카노": 4000}

my_cafe = Cafe(menu)

# 클래스 외부에서 업데이트
menu.update({"소주": 4500})

# 업데이트 반영 여부 확인
print(my_cafe.menu)

결과: {'아메리카노': 4000, '소주': 4500}
- 클래스 외부에서의 객체 업데이트가 클래스 내부에도 반영되어 버림
- 따라서 mutable 객체는 외부 업데이트로부터 영향받지 않도록 보호하기 위해 새로운 객체를 생성하여 사용하는 것이 좋다.
"""

# mutable 객체를 새로 생성하여 외부 업데이트로부터 보호
class Cafe:
    def __init__(self, menu):
        self.menu = dict(menu) # 내용만 복사하여 새로운 객체 생성

menu = {"아메리카노": 4000}
my_cafe = Cafe(menu)
menu.update({"소주": 4500})

print(my_cafe.menu)

"""
기본값 매개변수
- 함수를 정의할 때 매개변수에 기본값을 설정할 수 있음
- 기본값을 설정하면 인자가 전달되지 않을 때 자동으로 설정됨
"""

# 기본값 매개변수를 가지는 함수

def print_numbers(stop, step=1): # step 매개변수의 기본값 설정하여 인자를 받지 못하면 1로 자동설정
    print(list(range(0, stop, step)))

print_numbers(5)
print_numbers(10, 3)
