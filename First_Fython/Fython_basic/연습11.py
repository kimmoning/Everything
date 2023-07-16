# from logging import exception


# try:
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))  #내부에 오류가 생기면 밸류에러값을 송출
# except ValueError:                             #인트는 실수형을 정수형으로 바꿔주는건데 문자형 넣으면 당연히 오류 나지
#     print("에러! 잘못된값을 입력하였습니다")
# except ZeroDivisionError as err:                     #숫자 나누기 0 하면 생기는 오류임 
#     print(err)            #에러를 출력하게됨

# try:
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     #print("{0} / {1} = {2}".format(num1, num2, int(num1/num2))) 실수로 여기를 안썻다 가정했을떄
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:  
#     print(err)
# except Exception as err:       #어떤에러인지 알고싶으면 저 익셉션쓰면됨,위의 밸류에러,제로디비전에러뺴고 나머지 모든에러들은 이걸로 
#     print("알수없는 에러가 발생하였습니다")
#     print(err)

#에러 발샌시키기 
from logging import exception

#사용자 정의 예외 처리
class BigNumherettor(Exception):      #익셉션은 파이썬에 기본으로 제공하는 클래스래
    pass                     #익셉션은 앞에서 봤던 ValueError, IndexError 와 비슷하게 사용자가 필요로 하는 어떤 새로운 형태의 Error 를 정의할 수 있습니다



try:
    print("한자리 숫자 나누기 전용 계산기 입니다")
    num1=int(input("첫번쨰 숫자를 입력하세요:"))
    num2=int(input("두번쨰 숫자를 입력하세요:"))
    if num1 >= 10 or num2 >= 10 :
        raise BigNumherettor
    print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
except ValueError:                                             #레이즈를 통해서 에러를 만들수있음
    print("잘못된 값을 입력하였습니다.한자리 숫자만 입력하세요")
except BigNumherettor:
    print("에러가 발생하였습니다. 한자리 숫자만 입력하세요")



































