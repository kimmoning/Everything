
#해야할것 "(" 이거 입력하면 "()(" 이 나옴 이거 수정하고 ++ ")"을 입력해야 "()" 이 나올수 있게 이거만 그런게 아니고 쉬프트 누르는거 다그럼 입라
#했는데 수정가능하면할것 +++ 이거 쌍따음표하고 겹처서 일단 주석처리해놈 ,
# 내가 구현하는 함수들 설명창에다가 쓰기,나머지 구현안한 함수들 그 노트 찿아서 만들기,
#그리고 왠지는 모르겠는데 터치하는 실행으로 실행이 안되고 F5 눌러야 됨 수정가능하면 할것
from tkinter import*

root = Tk()
root.title("파이썬 IDE 입니다")
root.geometry("1250x650")
#root.geometry("480x480")
root.resizable(False, False)

설명창 = Label(root,text="파이썬 IDE 입니다 가운데 창에 코드를 입력하시면 됩니다\n\n--------------------------사용방법--------------------------\n\n1. 함수 단축키는 Alt + (원하는 함수의 첫번째 글자) 입니다.\n2. 앞에 .이 쓰이는 함수((ex).expend() 등등)은 Control + \n    (.을 제외한 원하는 함수의 첫번쨰 글자) 입니다.\n쌍따음표는 평소처럼 Shift + \" 를 입력하시면됩니다\n\n--------------------------주의사항---------------------------\n\n1. 함수단축키는 코드 가장 마지막에서만 사용해주세요\n2. Ctrl과 함께 괄호,중괄호,대괄호를 치면 괄호를 닫습니다.\n\n--------------------지원하는 단축키목록--------------------\n\n .find( ) , .join( ) , .upper( ) , .lower( ) , .Istrip( ) , .remove( ) , \n .split( ) , .pop( ) .count( ) , .get( ) , .add( ) , if , for , whlie , \n def , print , len , type , elif , False , break , return , and , or ,\n not ",justify="left")
설명창.place(x=25,y=30)

번호 = Label(root,text="1]\n2]\n3]\n4]\n5]\n6]\n7]\n8]\n9]\n10]\n11]\n12]\n13]\n14]\n15]\n16]\n17]\n18]\n19]\n20]\n21]\n22]\n23]\n24]\n25]\n26\n27]\n28]\n29]\n30]\n31]\n32]\n33]\n34]\n35]\n36]\n37]\n38]\n39]\n40]".rjust(3))
번호.place(x=920,y=10)

번호.configure(font=("Courier", 8   , "italic"))

입력창 = Text(root,width=70,height=48)
입력창.pack()
    
저작권안내 = Label(root,text="Copyright 2022.(오정현) all rights reserved.",justify="left")
저작권안내.pack()
    
출력창 = Label(root,text="코드입력시 이곳에 출력됩니다",justify="left")
출력창.place(x=950,y=10)
    

def 함수1 (event):
    global 입력창
    global 출력창
    global 입력값
    입력값 = 입력창.get("1.0", END)
    출력창.config(text=입력값)      

def 함수print (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("p")
    입력값 =(입력값+"print")    
    입력창.insert(END,"print")
    출력창.config(text=입력값)


def 함수if (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("i")
    입력값 =(입력값+"if")    
    입력창.insert(END,"if")
    출력창.config(text=입력값)

def 함수for (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("f")
    입력값 =(입력값+"for")    
    입력창.insert(END,"for")
    출력창.config(text=입력값)
#
def 함수whlie (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("w")
    입력값 =(입력값+"whlie")    
    입력창.insert(END,"whlie")
    출력창.config(text=입력값)

def 함수def (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("d")
    입력값 =(입력값+"def")    
    입력창.insert(END,"def")
    출력창.config(text=입력값)

##
def 함수len (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("l")
    입력값 =(입력값+"len")    
    입력창.insert(END,"len")
    출력창.config(text=입력값)

def 함수type (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("t")
    입력값 =(입력값+"type")    
    입력창.insert(END,"type")
    출력창.config(text=입력값)

def 함수True (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("T")
    입력값 =(입력값+"True")    
    입력창.insert(END,"True")
    출력창.config(text=입력값)

def 함수elif (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("e")
    입력값 =(입력값+"elif")    
    입력창.insert(END,"elif")
    출력창.config(text=입력값)

def 함수str (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("s")
    입력값 =(입력값+"str")    
    입력창.insert(END,"str")
    출력창.config(text=입력값)

def 함수False (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("F")
    입력값 =(입력값+"False")    
    입력창.insert(END,"False")
    출력창.config(text=입력값)
###
def 함수break (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("b")
    입력값 =(입력값+"break")    
    입력창.insert(END,"break")
    출력창.config(text=입력값)

def 함수return (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("r")
    입력값 =(입력값+"return")    
    입력창.insert(END,"return")
    출력창.config(text=입력값)

def 함수and (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("a")
    입력값 =(입력값+"and")    
    입력창.insert(END,"and")
    출력창.config(text=입력값)

def 함수or (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("o")
    입력값 =(입력값+"or")    
    입력창.insert(END,"or")
    출력창.config(text=입력값)

def 함수not (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("n")
    입력값 =(입력값+"not")    
    입력창.insert(END,"not")
    출력창.config(text=입력값)


####


def 함수remove (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값 =(입력값+".remove()")    
    입력창.insert(END,".remove()")
    출력창.config(text=입력값)

def 함수쌍콤마 (event):          #쌍콤마 용
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("\"")
    입력값 =(입력값+"\"")    
    입력창.insert(END,"\"")
    출력창.config(text=입력값)
#

def 함수find (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("f")
    입력값 =(입력값+".find()")    
    입력창.insert(END,".find()")
    출력창.config(text=입력값)


def 함수insert (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값 =(입력값+".insert()")    
    입력창.insert(END,".insert()")
    출력창.config(text=입력값)

def 함수join (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값 =(입력값+".join()")    
    입력창.insert(END,".join()")
    출력창.config(text=입력값)
##
def 함수upper (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값 =(입력값+".upper()")    
    입력창.insert(END,".upper()")
    출력창.config(text=입력값)
    
def 함수lower (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값 =(입력값+".lower()")    
    입력창.insert(END,".lower()")
    출력창.config(text=입력값)
    
def 함수Istrip (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값 =(입력값+".Istrip()")    
    입력창.insert(END,".Istrip()")
    출력창.config(text=입력값)
    
def 함수split (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값 =(입력값+".split()")    
    입력창.insert(END,".split()")
    출력창.config(text=입력값)
    
def 함수pop (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값 =(입력값+".pop()")    
    입력창.insert(END,".pop()")
    출력창.config(text=입력값)

def 함수count (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값.rstrip("c")
    입력값 =(입력값+".count()")    
    입력창.insert(END,".count()")
    출력창.config(text=입력값)

def 함수get (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값 =(입력값+".ger()")    
    입력창.insert(END,".get()")
    출력창.config(text=입력값)
    
def 함수add (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값 =(입력값+".add()")    
    입력창.insert(END,".add()")
    출력창.config(text=입력값)
   
def 함수괄호 (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값 =(입력값+"()")    
    입력창.insert(END,"()")
    출력창.config(text=입력값)
   
def 함수중괄호 (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값 =(입력값+"{}")    
    입력창.insert(END,"{}")
    출력창.config(text=입력값)
   
def 함수대괄호 (event):
    global 입력값 
    global 입력창
    global 출력창 
    입력값 =(입력값+"[]")    
    입력창.insert(END,"[]")
    출력창.config(text=입력값)

###

입력창.bind("<Key>",함수1)    #전체 값 받기 
입력창.pack()

입력창.bind("<Alt-p>",함수print) #print 용 
입력창.pack()


입력창.bind("<Alt-i>",함수if) #if 용 
입력창.pack()

입력창.bind("<Alt-f>",함수for)  
입력창.pack()
#
입력창.bind("<Alt-w>",함수whlie)  
입력창.pack()

입력창.bind("<Alt-d>",함수def)  
입력창.pack()

##

입력창.bind("<Alt-l>",함수len)  
입력창.pack()

입력창.bind("<Alt-t>",함수type)  
입력창.pack()

입력창.bind("<Alt-T>",함수True)  
입력창.pack()

입력창.bind("<Alt-e>",함수elif)  
입력창.pack()

입력창.bind("<Alt-s>",함수str)  
입력창.pack()

입력창.bind("<Alt-F>",함수False)  
입력창.pack()
###

입력창.bind("<Alt-b>",함수break)  
입력창.pack()

입력창.bind("<Alt-r>",함수return)  
입력창.pack()

입력창.bind("<Alt-a>",함수and)  
입력창.pack()

입력창.bind("<Alt-o>",함수or)  
입력창.pack()

입력창.bind("<Alt-n>",함수not)  
입력창.pack()
###################################################
입력창.bind("<Control-(>",함수괄호) # () 용
입력창.pack()

입력창.bind("<Control-{>",함수중괄호) # () 용
입력창.pack()

입력창.bind("<Control-[>",함수대괄호) # () 용
입력창.pack()


입력창.bind("<Control-r>",함수remove) 
입력창.pack()

입력창.bind("<Shift-\">",함수쌍콤마) # " 용
입력창.pack()
#
입력창.bind("<Control-f>",함수find) 
입력창.pack()

입력창.bind("<Control-i>",함수insert) 
입력창.pack()

입력창.bind("<Control-j>",함수join) 
입력창.pack()
##

입력창.bind("<Control-u>",함수upper) 
입력창.pack()

입력창.bind("<Control-l>",함수lower) 
입력창.pack()

입력창.bind("<Control-I>",함수Istrip) 
입력창.pack()
###

입력창.bind("<Control-s>",함수split) 
입력창.pack()

입력창.bind("<Control-p>",함수pop) 
입력창.pack()

입력창.bind("<Control-c>",함수count) 
입력창.pack()

입력창.bind("<Control-g>",함수get) 
입력창.pack()

입력창.bind("<Control-a>",함수add) 
입력창.pack()


root.mainloop()
