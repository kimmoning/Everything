#표준 입출력

"""import sys
print("python","java",file=sys.stdout)   #둘다 똑같이 출력됨 그러나 실제로는 얘는 표준출력으로 문장이 찍히는거고
print("python","java",file=sys.stderr)   #얘는 표준 에러로 처리된다 잘모르겠는데 만약에 로고 처리를 따로한다고 할때 표준출력은 잘 출력돼는데 에러는 프로그램을 확인을 해서 프로그램코드를 수정하든지해야함 그럴때stderr 쓰면됨   



print("python","java","javascript" ,sep=" , ",end="?")     #sep=" , " 하면 파이썬하고 자바 하고 자바스립트 사이에 , 이게 들어감
print("무엇이 더 재밌을까요?") """     #엔드 쓰니깐 이 두개가 한줄로 나옴     #엔드는 파이썬,자바,자바스크립트의 문장 끝부분을 ?로 바꿔줌

# #출력 포맷
# # # 시험성적  
# # scores={"수학":0,"영어":50,"코딩":100}  #지금 딕셔너리여서 키와 밸류로 들어 가있다
# # for subject,score in scores.items():     #키와 밸류를 쌍으로 튜플로 보내준다 
# #   #  print(subject,score)              
# #     print(subject.ljust(8),str(score).rjust(4),sep=":")        #서브젝트 부분에서 8자리차지하고":"나오고스코어가 4칸 차지하고 오른쪽으로 붙어서 나온다 =가독성이 좋아 진다         

# #은행 대기 순번표
# # #001,002,003
# # for num in range(1,21):
# #     print("대기변호 : "+str(num).zfill(3))   #3크기만큼 확보하는데 빈자리는 0으로 채워준다는 의미 
     
# # answer=input("아무 값이나 입력하세요 : ")  #대답하면 문자열 형태로 엔써에 들어감    
# # print(type(answer))

# #다양한 출력 포맷 
# #빈자리 빈공가능로 두고  오른쪽정렬을 하되 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# #양수일떈 +로 표시,음수일떈-로 표시 
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# #왼쪽 정렬하고,빈칸으로_로 채움
# print("{0:_<+10}".format(500))
# #3자리마다 콤마를 찍어주기
# print("{0:,}".format(100000000000000))  #왜 3자리씩인지는모르겠네;;
# #3자리마다 콤마를 찍어주기,+-부호도 붙히기
# print("{0:+,}".format(-100000000000000))  
# print("{0:+,}".format(100000000000000))  #왜 3자리씩인지는모르겠네;;
# #3자리마다 콤마를 찍어주기,부호도 붙히기,자릿수 확보하기
# #돈이 많으면 행복하니깐 빈자리는 ^로 채우기
# print("{0:^<+30,}".format(10000000000))

# #소수점 출력
# print("{0:f}".format(5/3))
# #소수점 특정 자리 수까지만 표현
# print("{0:.2f}".format(5/3))   #소수점 둘째 자리수까지 표현 수수점 3번째에서 반올림

# #파일 입출력
# score_flie=open("score.txt","w",encoding="utf8")   #대충 대른데서 파일 불러온다는 의미 인듯 w 저거 쓰면 이파일은 쓰기위한목적으로 열겠다 정의 해주는거임 저거 utf8은 한글정보,한글을썻을때 제대로 나옴
# print("수학:0",file=score_flie)
# print("영어=50",file=score_flie)
# # score_flie.close()                   #이거 실행시켜서 스코어 점 텍스라는 파일이 생김 니가 가서 봐봐

# score_flie=open("score.txt","a",encoding="utf8")   #이미 존재하는 파일에다가 쓰고싶으면 저 a를쓰면됨
# score_flie.write("과학:80")
# score_flie.write("\n코딩:100")                  #저 write 를써주면 줄바꿈이 따로 없음 저 n 이 줄바꿈일꺼임  
# score_flie.close()

# score_flie=open("score.txt","r",encoding="utf8")      #이 r은 리드를 뜻하는것으로 파일을 읽어 온다는뜻
# print(score_flie.read())         #파일의 모든내용을 출력해줌
# score_flie.close()

# #한줄한줄불러오고싶다 
# score_flie=open("score.txt","r",encoding="utf8")
# print(score_flie.readline())       #줄별로 읽기 ,한줄읽고 커서는 다음줄로 이동
# print(score_flie.readline())  
# print(score_flie.readline())          #프린트에선 자동으로 줄바꿈을 해주기 떄문에 한줄씩 띄어져서 나온다 그게 싫으면
# print(score_flie.readline())              #print(score_flie.readline(),end="")   쓰면됨  
# score_flie.close()

# #위에는 네줄인걸 알아서 스코어 파일 리드라인을 네번썻지만 모를때 쓰는방법

# score_flie=open("score.txt","r",encoding="utf8")
# while True:
#     line=score_flie.readline()
#     if not line:
#         break
#     print(line,end="")         #줄바꿈안하고 싶으면 저 엔드 써주고 
# score_flie.close()


# score_flie=open("score.txt","r",encoding="utf8")
# lines=score_flie.readlines()    #가저온 모든걸 리스트 형태로 저장
# for line in lines:
#     print(line,end="")
# score_flie.close()        #파일 닫는거 잊지마

# #pickle    프로그램상에서 우리가 사용하던 데이터를 파일의 형태로 저장해줌 누가 받으면 그이도 피클로 데이터를 가지고와 코드에서 씀
# import pickle
# # proflie_flie=open("profile.pickle","wb")    #b 는 바이너리를 의미,피클을 쓰기위해선항상 바이너리 타입으로 정의 해줘야함   바이너리=이진법   
# # proflie={"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
# # print(proflie)
# # pickle.dump(proflie,proflie_flie)  #피클을 이용해서 이데이터를 파일에 씀,프로필에 있는 정보를 flie에 저장 
# # proflie_flie.close()

# proflie_flie=open("profile.pickle","rb") 
# proflie=pickle.load(proflie_flie)                     #파일에 있는 내용을 그대로 가져와서 데이터형태로 불러와준다 ,파일에 있는 내용을 프로필에 불러오기 
# print(proflie)
# proflie_flie.close()

#with  위드 쓰면 위의 작업을 더 편하게 쓸수있데
# import pickle
# with open("profile.pickle","rb") as proflie_flie:
#     print(pickle.load(prfile_flie))                #이전에 만들었던 profile.pickle이 나옴 클로즈 따로 써줄필요 없대 위드문 탈줄 하면서 자동으로 클로즈됨

#피클 안쓰고 일반적인 파일을 쓰고 읽는걸 위드를활용해서
# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())                                   

















