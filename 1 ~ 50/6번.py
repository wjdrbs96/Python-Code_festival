#게임 캐릭터 클래스 만들기
#class 에서 __init__ 의 사용법을 알아두자
class Wizard:
    def __init__(self,health, mama,armor):
        self.health = health;
        self.mama = mama;
        self.armor = armor;

    def attack(self):
        print("파이어볼")

x= Wizard(health = 545, mama =210, armor = 10)
print(x.health, x.mama, x.armor)
x.attack()
