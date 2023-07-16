
#if
#weather="비"
#if weather=="비":   #== 이건 앞뒤가 같으면 트루 출력해줌    실행 명령문 이조건에 해당돼면 실행돼
#    print("우산을 챙기세요")


weather="비"
if weather=="비":
    print("우산을 챙기세요")
elif weather=="미세먼지":
    print("마스크를 챙기세요")
else :
    print("준비물 필요 없어용")    #우산을 챙기세요 출력

weather="미세먼지"
if weather=="비":
    print("우산을 챙기세요")
elif weather=="미세먼지":
    print("마스크를 챙기세요")
else :
    print("준비물 필요 없어용")    #마스크를 챙기세요 출력


weather="맑아요"
if weather=="비":
    print("우산을 챙기세요")
elif weather=="미세먼지":
    print("마스크를 챙기세요")
else :
    print("준비물 필요 없어용")     #준비물필요 없어요 출력


weather=input("오늘날씨는 어때요")     #인풋 이라고 사용자 입력 받는거임 나중에 배운데 오늘쌀씨는 어때요 물어보고 내가 비라고 말하면 우산을 챙기세요 라고 말함
if weather=="비" or weather=="눈":    #비가오면 이였는데 비가 오거나 눈이 오면으로 됨 or은 
    print("우산을 챙기세요")
elif weather=="미세먼지":
    print("마스크를 챙기세요")
else :
    print("준비물 필요 없어용") 

temp=int(input("기온은 어때요?"))     #기온은 보통 숫자인데 인풋은 문자열로 값을 받기때문에 int로 바꿔줌 int는 정수형으로 바꿔주는거임
                                      #입력받은값을 정수형태로 바꿔서 템포로 지정
if 30<= temp:                          #30보다 크면 이라는 뜻임           
    print("너무더워 나가지마")
elif 10<=temp and temp<30:            # < 이건 미만임 
    print("괜찬은 날씨에요")
elif 0 <=  temp <10 :                #이렇게 and 없에도 돼 
    print("외투를 챙기세요")
else :
    print("너무 추워요 나가지말아요")      #else 는 if not 인듯

#for

"""
print("대기번호 :1")
print("대기번호 :2")
print("대기번호 :3")          #이런게 100번 천번이면힘드니깐도와주는 for문임
print("대기번호 :4")




#randrange()    
for Waiting_no in range(1,6) :     #1부터6미만    #여기서 웨이팅노 에 0에서 5까지 순서대로 나온수 하나 씩 들어가는거임
    print("대기번호:{0}".format(Waiting_no))    


starbucks=["아이언맨","토르","그루트"]
for customer in starbucks:
    print("{0},커피가 준비돼었습니다.".format(customer))

#while 문 

customer ="토르"
index=5
while index >= 1 :
    print("{0},커피가 준비돼었습니다.{1}번 남았어요".format(customer,index))
    index -=1        #-= 1 은 1을 뺀다는거임 
    if index ==0:
        print("커피는 폐기처분 되었습니다.")


customer="아이언맨"
index=1
while True:
    print("{0},커피가 준비돼었습니다.호출{1}회".format(customer,index))
    index += 1
"""

customer="토르"
person="unknown"

while person !=customer :    #!= 부등호임
    print("{0},커피가 준비돼었습니다.".format(customer))
    person=input("이름이 어떻게 돼세요?")          #펄슨에 사람이름넣고 부등호니깐 토르 아니면 펄스돼서 와일문 반복


#continue와 break
absant=[2,5]  #결석
no_book=[7]   #책을 깜박함
for student in range(1,11):    #1,2,3,4,5,6,7,8,9,10 
    if student in absant:
        continue               #그니깐 컨티뉴는 스킵이라 볼수있지
    elif student in no_book:
        print("오늘수업여기까지.{0}는 교무실로 따라와".format(student))
        break         #6까지 하다가 7차례때 교무실감
    print("{0},책을 읽어봐".format(student))      #2,5빼고 전부출력됨



#출석번호가 1 2 3 4,앞에 100을 붙이기로 함 ->101,102,103,104.
"""
student=[1,2,3,4,5]
print(student)
student=[i+100 for i in student]
print(student)

# 학생이름을 길이로 변환    
student=["아이언맨","토르","그루트"]    #얘네는 이름길이를 하나씩세주는거임     
student=[len(i)for i in student]
print(student)
"""
#학생이름을 대문자로 변환
student=["아이언맨","토르","그루트"]
student=[i.upper()for i in student]    #영어 일때 얘네들을 대문자로 하나씩 바꿔주는거임
print(student)





















