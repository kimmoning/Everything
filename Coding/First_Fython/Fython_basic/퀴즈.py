#퀴즈 3
url="http://naver.com"
my_str=url.replace("http://","") #규칙 1
print(my_str)
my_str=my_str[0:my_str.index(".")] #my_str에서 []안에는 naver.com에서 r까지만 필요함 그니깐 0:5이여야 하지 그래서0쓰고:쓰고 뒤에 my_str.index(".")은 naver.com에서 .의 위치(5)를 나타내므로 [0:5가]되어 naver가 나옴 
print(my_str)
password=my_str[0:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print(url+"의 비밀번호는"+password+"입니다")


#퀴즈4
from random import*

user=range(1,21)  #1부터20 숫자 생성   
print(type(user))    #타입이 레인지로 나옴 리스트로 바꿔줄필요가 있음
user=list(user)      #리스트타입으로 변환   

print("당첨자"+(str(user)))

#정답 
user=range(1,21)
user=list(user)  
winner=(sample(user,4))


print("--당첨자 발표--")
print("치킨 당첨자:{0}".format(winner[0]))
print("커피당첨자:{0}".format(winner[1:]))  #1:옆에 숫자 써봐라 모르겠으면
print("--축하합니다--")

#퀴즈 5
from random import*
cnt=0 #총탑승객수
for i in range(1,51):   #1에서 50이라는수 (승객)
    time=randrange(5,51)   #5분에서 50분 소요시간
    if 5<= time <=15:         #5분에서 15분이내의 손님,탑승수 증가 처리 
        print("[o]{0}번째 손님 (소요시간:{1}분)".format(i,time))
        cnt +=1
    else:     #매칭실패한경우
        print("[ ]{0}번째 손님 (소요시간:{1}분)".format(i,time))

print("총 탑승 승객:{0}분".format(cnt))

#퀴즈 6

def str_weight(height,gender):
    if gender=="남자":  
        return height*height*22
    else:    
        return height*height*21
height=175
gender="남자"
weight=round(str_weight(height/100, gender),2)
print("키{0}의 {1}남자의 표준 체중은 {2}입니다".format(height,gender,weight))



#퀴즈 7 



for i in range(1,51):
    with open(str(i)+"주차.txt","w",encoding="utf8") as profile:
        profile.write("-{0}주차 주간 보고-".format(i))             
        profile.write("\n부서:")
        profile.write("\n이름:")
        profile.write("\n업무 요약:")























