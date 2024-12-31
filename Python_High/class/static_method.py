"""
정적 메서드
- 클래스나 인스턴스의 영향을 미치지 않는 독립적인 메서드를 말함
- '@staticmethod' 데코레이터를 사용하여 정적 메서드임을 명시
- 속성과 상관없는 동작을 하기 때문에 매개변수로 self나 cls 사용 X
- 클래스에 속해 있으므로, '클래스명.메서드명()'과 같이 클래스 이름을 통해 호출
"""

# 정적 메서드를 포함하는 클래스
class Car:
    def __init__(self, color, engine):
        self.color = color
        self.engine = engine

    # 정적 메서드를 의미하는 데코레이터
    @staticmethod
    # 클래스나 인스턴스에 영향을 주지 않는 기능을 수행하는 메서드
    def convert_km_to_mi(km):
        mi = km * 0.6214
        print(f"{km}km는 {mi:.2f}마일")

# 정적 메서드 호출
Car.convert_km_to_mi(10)
Car.convert_km_to_mi(20)
Car.convert_km_to_mi(30)

"""
@staticmethod
def display_info(self): # self 매개변수가 전달되지 않음
    print(f"색깔: {self.color}\n엔진: {self.engine}")

- 정적 메서드에서는 self 매개변수가 자동으로 전달되지 않으므로, 접근 시도 X
"""