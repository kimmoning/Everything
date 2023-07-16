# #클래스
# name="마린"
# hp=40
# damage=5
# print("{0}유닛이 생성되었습니다".format(name))
# print("체력{0},공격력{1}\n".format(hp,damage))
# 메소드(Method)
# 메소드는 함수와 비슷하다.
# 클래스에 묶여서 클래스의 인스턴스와 관계되는 일을 하는 함수
# tank_name="탱크"
# tank_hp=150
# tank_damage=35
# # print("{0}유닛이 생성되었습니다".format(tank_name))
# # print("체력{0},공격력{1}\n".format(tank_hp,tank_damage))

# # tank2_name="탱크"
# # tank2_hp=150
# # tank2_damage=35
# # print("{0}유닛이 생성되었습니다".format(tank2_name))
# # print("체력{0},공격력{1}\n".format(tank2_hp,tank2_damage))

 
# # def attack(name,location,damage):
# #     print("{0}:{1} 방향으로 적군을 공격합니다.[공격력{2}]".format(name,location,damage))      #유닛이 수백개면 일일히 만들기 버거움 그래서 필요한게 클래스

# # attack(name, "1시", damage)
# # attack(tank_name, "1시", tank_damage)
# # attack(tank2_name, "1시", tank2_damage)      #클래스는 붕어빵 틀로 비유한다네 일반적으로 변수와 함수의 집합정도로 이해하시면된데
#일반유닛
# class unit: 
#     def __init__(self,name,hp,damage):                 #init 는 나중에 가르쳐준데
#          self.name=name
#          self.hp=hp
#          self.damage=damage
#          print("{0}유닛이 생성되었습니다".format(self.name))          #유닛 이라는 클래스가 만들어 진거임
#          print("체력{0},공격력{1}".format(self.hp,self.damage))   
# marine1=unit("마린", 40, 5)
# marine2=unit("마린", 40, 5)
# tank=unit("탱크", 150, 35)   #일부만 넘기면 사용이 불가함

# #__init__ 파이썬 에서 쓰이는 생성자래 생성자(영어: constructor, 혹은 약자로 ctor)는 객체 지향 프로그래밍에서 객체의 초기화를 담당하는 서브루틴을 가리킨다. 생성자는 객체가 처음 생성될 때 호출되어 멤버 변수를 초기화하고, 필요에 따라 자원을 할당하기도 한다. 객체의 생성 시에 호출되기 때문에 생성자라는 이름이 붙었다

# wraith1=unit("레이스",80,5)
# print("유닛이름:{0},공격력:{1}".format(wraith1.name,wraith1.damage))

# wraith2=unit("빼앗은레이스",80,5)
# wraith2.clocking=True
 
# if wraith2.clocking==True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))


# # #공격유닛
# class attackunit: 
#     def __init__(self,name,hp,damage):               
#          self.name=name
#          self.hp=hp                        #셀프는 자기자신을의미 메소드앞에는 항상 셀프를 붙혀 셀프.~로 자기자신의 변수에 접근할수있는거임   
#          self.damage=damage
#     def attack(self,location):                  #셀프 붙힌 네임과 데미지는 위에 클래스에 만들어둔 셀프.네임,셀프.데미지에서 값을가져오고 로케이션은 셀프가 없으므로 그위의 함수에서 값을가져온다
#         print("{0}:{1} 방향으로 적군을 공격합니다.[공격력{2}]".format(self.name,location,self.damage))
#     def damaged(self,damage):
#         print("{0}:{1}데미지를 입었습니다".format(self.name,damage))
#         self.hp -= damage
#         print("{0}:현재 체력은 {1} 입니다".format(self.name,self.hp))
#         if self.hp <=0:
#             print("{0} : 파괴되었습니다".format(self.name))

# #파이어뱃 
# firebat1= attackunit("파이어뱃",50,16)
# firebat1.attack("5시")

# #공격두번받는다 가정
# firebat1.damaged(25) 
# firebat1.damaged(25)

#상속
#메딕:의무병         메딕은 공격력이 없어서 데미지 부분뺴줌
class unit: 
    def __init__(self,name,hp,speed):                 #init 는 나중에 가르쳐준데
         self.name=name
         self.hp=hp 
         self.speed=speed
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
# #파이어뱃 
# firebat1= attackunit("파이어뱃",50,16)
# firebat1.attack("5시")

# #공격두번받는다 가정
# firebat1.damaged(25) 
# firebat1.damaged(25)

#다중상속 :부모 클래스를 두개 이상 상속받음
#날수있는 기능을 가진 클래스
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




# valkyrie = flyableattackunit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name,"3시")   

#연산자 오버로딩 부모클래스 말고 자식 클래스 사용하고 싶을때 메소드를 새롭게 정의해서 사용할수있는데 이를 오버로딩이라 한다
#벌쳐
vulture=attackunit("벌쳐", 80, 10, 20)
#배틀크루저
battlecruiser=flyableattackunit("배틀크루저", 500, 25,3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name,"9시")   #이렇게 따로 지상유닛속도,공중유닛속도 지정하면 귀찬음 그래서필요한게 연산자 오버로딩 똑같이 무브함수만 이용해서 해보자
battlecruiser.move("9시")

#pass 
#건물 
class buildingunit(unit):
    def __init__(self, name, hp, location): 
        #unit.__init__(self, name, hp,speed)                          
        super().__init__( name, hp,speed)              #수퍼 쓸때는 위뜨 쓰면 안됨              
        
        self.location=location


#서플라이 디폿
supply_depot=buildingunit("서플라이 디폿", 500,"7시")
def game_start():
    print("[알림] 새로운게임을 시작합니다.")
def game_over():
    pass       
game_start()                                 #패스는 일단완성된거 처럼보이는거임 에러는 안뜸
game_over()
# #슈퍼 

class unit:
    def __init__(self):
        print("유닛생성자")

class flyable:
    def __init__(self):
        print("flyable 생성자")
class flyableunit(unit,flyable): 
    def __init__(self):
        #super().__init__()       #두개이상의 부모 클래스를 상속받을때 슈퍼를쓰면 맨마지막에 상속받는 클래스에 대해서만 유닛함수가 호출된다
        unit.__init__(self)
        flyable.__init__(self)  #이런식으로 두번을 통해서 초기화를 하는방식을 사용
#드랍쉽
dropship=flyableunit()  







































































































