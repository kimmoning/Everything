from tkinter import*
from math import*

root = Tk()
root.title("단리복리계산기 입니다")
root.geometry("640x480")

원금입력요구창 = Label(root,text="원금(만원)을 입력하세요")
원금입력요구창.pack()

원금입력창 = Entry(root,width=20)
원금입력창.pack()
    
def cmd1():
    global 원금입력창
    global 원금
    원금 = float(원금입력창.get()) 
    print("입력된 원금은 {0}만원 입니다".format(원금))
    원금입력창.delete(0,END)
    
btn1 = Button(root, text="확인",command = cmd1)
btn1.pack()

이율입력요구창 = Label(root,text="이율(%)을 입력하세요")
이율입력요구창.pack()

이율입력창 = Entry(root,width=20)
이율입력창.pack()

def cmd2():
    global 이율입력창
    global 이율
    이율 = float(이율입력창.get()) 
    print("입력된 이율은 {0}% 입니다".format(이율))
    이율입력창.delete(0,END)

btn2 = Button(root, text="확인",command = cmd2)
btn2.pack()

기간입력요구창 = Label(root, text="기간(년)을 입력하세요")
기간입력요구창.pack()

기간입력창 = Entry(root,width=20)
기간입력창.pack()

def cmd3():
    global 기간입력창
    global 기간
    기간 = float(기간입력창.get()) 
    print("입력된 기간(년)은 {0} 입니다".format(기간))
    기간입력창.delete(0,END)

btn3 = Button(root, text="확인",command = cmd3)
btn3.pack()

단리복리 = Label(root,text="단리,복리를 선택하세요")
단리복리.pack()

def cmd단리 ():
    global 원금
    global 이율
    global 기간
    단리이자 = (원금+이율*기간)
    print(단리이자)

단리버튼 = Button(root,text="단리",command= cmd단리)
단리버튼.pack()

def cmd복리 ():
    global 원금
    global 이율
    global 기간
    복리이자 = (원금*(1+(이율/100))**기간)
    print(round(복리이자,2))

복리버튼 = Button(root,text="복리",command= cmd복리)
복리버튼.pack()
 
root.mainloop()

