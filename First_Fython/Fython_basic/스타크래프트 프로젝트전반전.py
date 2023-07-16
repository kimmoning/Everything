from random import*
class unit: 
    def __init__(self,name,hp,speed):                 #init 는 나중에 가르쳐준데
         self.name=name
         self.hp=hp 
         self.speed=speed
         print("{0}유닛이 생성되었습니다".format(name))
    def move(self,location):
        print("[지상유닛 이동]")
        print("{0}:{1} 방향으로 이동합니다.[속도{2}]".format(self.name,location,self.speed))
        
                                #보다시피 겹치는 부분이많음 이럴떈 상속을써야함 및에 꺼가 상속쓴거임
class attackunit(unit): 
    def __init__(self,name,hp,speed,damage):               
        unit.__init__(self, name, hp,speed)                                                                             #셀프는 자기자신을의미 메소드앞에는 항상 셀프를 붙혀 셀프.~로 자기자신의 변수에 접근할수있는거임   
        self.damage=damage
    def attack(self,location):                  #셀프 붙힌 네임과 데미지는 위에 클래스에 만들어둔 셀프.네임,셀프.데미지에서 값을가져오고 로케이션은 셀프가 없으므로 그위의 함수에서 값을가져온다
        print("{0}:{1} 방향으로 적군을 공격합니다.[공격력{2}]".format(self.name,location,self.damage))
    def damaged(self,damage):
        print("{0}:{1}데미지를 입었습니다".format(self.name,damage))
        self.hp -= damage
        print("{0}:현재 체력은 {1} 입니다".format(self.name,self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다".format(self.name))

class flyable:
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed
    def fly(self,name,location):
        print("{0}:{1}방향으로 날아갑니다.[속도{2}]".format(name,location,self.flying_speed))
#공중 공격 유닛 클래스
class flyableattackunit(attackunit,flyable):
    def __init__(self, name, hp, damage,flying_speed):
        attackunit.__init__(self,name, hp,0, damage)       #지상 스피드는 0으로 처리
        flyable.__init__(self, flying_speed)
    def move(self, location):
        print("[공중유닛이동]") 
        self.fly(self.name, location)      

#마린
class Marine(attackunit):
    def __init__(self):
        attackunit.__init__(self, "마린", 40, 1, 5)
#스팀팩
    def stimpack(self):
        if self.hp > 10:
            self.hp -=10
            print("{0} 유닛이 스팀팩을 사용합니다.[hp 10 감소]".format(self.name))
        else:
            print("{0}:체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))
#탱크
class Tank(attackunit):   #시즈모드
    seize_developed = False

    def __init__(self):
        attackunit.__init__(self, "탱크", 150, 1, 35)
    
    def set_seize_mode(self):
        if Tank.seize_developed==False:       #시즈모드 개발안됬으면 그냥 나간다
            return
        #현재 시즈모드가 아닐떄 ->시즈모드
            if self.sieze_mode == False:
                print("{0}:시즈모드로 전환합니다".format(self.name))
            self.damage *= 2
            self.seize_mode=True
         #현재 시즈모드일때 ->시즈모드 해제
        else:
            print("{0}:시즈모드를 해제 합니다".format(self.name))
            self.damage /= 2
            self.seize_mode=False
#레이스
class Wraith(flyableattackunit):
    def __init__(self):
        flyableattackunit.__init__(self,"레이스", 80, 20,5)
        self.clocked=False #클로킹 모드 (해제상태)
    def clocking(self):
        if self.clocked==True: #클로킹 모드 -> 모드 해제
            print("{0}:클로킹 모드 해제 합니다".format(self.name))
            self.clocked=False
        else: #클로킹 모드 해제 -> 모드 설정
            print("{0}클로킹 모드 설정합니다".format(self.name))
            self.clocked=False

#후반전
... # 클래스 생략 위에 있음

# 게임 시작
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

# 게임 종료
def game_over():
    print("Player : gg") # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()
# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t1) 
attack_units.append(w1)

#전군이동
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발 
Tank.seize_developed=True
print("[알림]탱크시즈모드 개발이완료되었습니다")
  
#인스턴스는 지금만들어진 객체가 어떤 클래스의 인스턴스인지 확인하는것
# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine): # Marine 의 인스턴스이면 스팀팩
        unit.stimpack()
    elif isinstance(unit, Tank): # Tank 의 인스턴스이면 시즈모드
        unit.set_seize_mode()
    elif isinstance(unit, Wraith): # Wraith 의 인스턴스이면 클로킹
        unit.clocking()
#전군공격
for unit in attack_units:
    unit.attack("1시")

#전군피해
for unit in attack_units:
    unit.damaged(randint(5,21))  #공격은 랜덤으로 받음 (5~20)

#게임종료
game_over()



























        