# #함수 
# def open_account():     #함수정의 할뗀 def써라
#     print("새로운계좌가 생성되었습니다")
# open_account()     #이래야지 출력됨
# #전달값과 반환값
# def deposit(balance,money):    #입금
#      print("입금이 완료되었습니다.잔액은{0}원입니다.".format(balance+money))
#      return balance+money
# balance=10 #잔액


# balance = deposit(balance, 1000)
# print(balance)

# def withdrew(balance,money):  #출금
#     if balance >=money #잔액이 출금보다 많으면 
#         print("출금이 완료돼었습니다,잔액은{0}원입니다.".format(balance-money))
#         return balance-money    
#     else



# gender=input("성별이 무엇입니다") 
# height=input("키는 얼맙니다") 
# height = float(height)
# #,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# def deposit(balance,money):    #입금
#      print("입금이 완료되었습니다.잔액은{0}원입니다.".format(balance+money))
#      return balance+money
# balance=10 #잔액


# balance = deposit(balance, 1000)
# print(balance)


# #https://blockdmask.tistory.com/440



# #함수 

# """def open_account():     #함수정의 할뗀 def써라

#     print("새로운계좌가 생성되었습니다")

# open_account()     #이래야지 출력됨

# #전달값과 반환값

# def deposit(balance,money):    #입금

#      print("입금이 완료되었습니다.잔액은{0}원입니다.".format(balance+money))

#      return balance+money

# balance=10 #잔액



# balance = deposit(balance, 1000)
# print(balance)


# def withdrew(balance,money):  #출금

#     if balance >=money: #잔액이 출금보다 많으면

#         print("출금이 완료돼었습니다,잔액은{0}원입니다.".format(balance-money))

#         return balance-money    

#     else:

#         print("출금불가.잔액은{0}원입니다".format(balance))

#         return balance



# def withdrew_night(balance,money): #저녁에 출금

#     commission=100 #수수료 100원

#     return commission,balance-money-commission


# balance=0

# balance=deposit(balance,1000)

# #balance=withdrew(balance, 2000)

# commission,balance=withdrew_night(blance, 500)

# print("수수료는{0}원 이며 잔액은{1}원 입니다 ".format(commission,balance))"""


# #항수 기본값

# #def profile(name,age,main_lang):

#     #print("이름:{0}\t나이:{1}\t주사용언어{2}"\

#         #.format(name,age,main_lang))          #역슬래쉬이거치면옆으로쓴거랑 똑갈이 취급됨

# #profile("유재석",20,"파이썬")

# #profile("김태호",25,"자바")


# #같은학교 같은 학년 같은 반 수업 


# #def profile(name,age=17,main_lang="파이썬"):

#     #print("이름:{0}\t나이:{1}\t주사용언어{2}"\

#     #    .format(name,age,main_lang))    

# #profile("유재석")

# #profile("김태호")


# #키워드값을 이용한 함수 호출

# #def profile(name,age,main_lang):

#     #print(name,age,main_lang)

# #profile(name="유재석",main_lang= "파이썬",age=20)

# #profile(main_lang="자바",age=25,name="김태호")       #키워드 값을 이렇게 하나하나 지정해주면 순서 상관x


# #가변인자를 이용한 함수호출

# #def proflie(name, age, end, lang1, lang2, lang3, lang4, lang5):
#     #print("이름:{0}\t나이:{1}\t".format(name,age),end=" ")  #이렇께 큰따음표 스페이스큰따음표 하면은프린트 문이 끝날때 줄바꿈안하고 그냥이렇게만 끝남
#     #print(lang1,lang2,lang3,lang4,lang5)
    
# """def profile(name,age,*language):
#         print("이름:{0}\t나이:{1}\t".format(name,age),end=" ")  #랭귀지가 가변인자로써 
#         for lang in language:
#             print(lang,end=" ")
#         print()                              #이거 줄바꿈이라는데 나도 자세히는몰겠다

# profile("유재석", 20, "파이썬", "자바", "씨", "씨플플", "씨샵", "자바스크립트")
# profile("김태호", 25, "kotlin", "swift")     #이거 두개만하는데 자리 5번 채워줘야하니깐 빈칸으로"""

# #지역 변수와 전역변수   #지역변수는 함수내에서만 쓸수있는거 함수호출이 끝나면 사라짐 전역변수는 프로그램 어디에서든지 불러올수있다 
# """gun=10

# def checkpoint(soldiers): #경계근무
#     gun=gun-soldiers                        #그냥 여기안에다가 건=10 넣으면 되긴함
#     print("[함수]내 남은총:{0}".format(gun))

# print("전체 총;{0}".format(gun))
# checkpoint(2)    #두명이 경계근무 나간다 가정        #오류뜸 왜냐하면 밖에 건을 10으로 지정 하였으나 함수내에선 지정이 안됨 이게 지역 변수
# print("남은 총;{0}".format(gun))"""

# gun=10

# def checkpoint(soldiers): #경계근무
#     global gun                                   #이 글로발 이라는키워드를 쓰면 위에 건=10이 사용됨
#     gun=gun-soldiers                       
#     print("[함수]내 남은총:{0}".format(gun))
                                               
# def checkpoint_ret(gun,soldiers):    #여기서 전달받은 건 자체도 함수 내에선 지역변수
#     gun=gun-soldiers                  
#     print("[함수]내 남은총:{0}".format(gun))
#     return gun  



# print("전체 총;{0}".format(gun))
# #checkpoint(2)    #두명이 경계근무 나간다 가정        
# gun=checkpoint_ret(gun,2)
# print("남은 총;{0}".format(gun))

















