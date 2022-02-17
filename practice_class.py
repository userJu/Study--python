class Unit:
  def __init__(self):
    print('Unit 생성자')


class Flyable:
  def __init__(self):
    print("Flyable 생성자")


class FlyableUnit(Unit, Flyable):
  def __init__(self):
    super().__init__()



dropship = FlyableUnit() # Unit 생성자
# 두 개 이상의 부모클래스를 다중으로 상속받을 때는 맨 처음의 class에 대해서만 나온다
# 따라서 하나만 있는게 아니라면 
# Unit.__init__(self)
# FlyableUnit.__init__(self)
# 이렇게 각각 연결해주는 것이 좋다
