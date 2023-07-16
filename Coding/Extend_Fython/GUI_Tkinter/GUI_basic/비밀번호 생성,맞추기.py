from tkinter import*
 
root = Tk()
root.title("비밀 번호를 입력하시면 숨겨진 사진이 나옵니다")
root.geometry("640x480")

img = PhotoImage(file="GUI_basic/img.png")
img1 = PhotoImage(file="GUI_basic/img1.png") 
img2 = PhotoImage(file="GUI_basic/img2.png")

label1 = Label(root,text="초기 비밀번호를 입력하세요")
label1.pack()

firstpassword = Text(root,width=20,height=7)
firstpassword.pack()

def cmd2():
    global password
    password = (firstpassword.get("1.0",END)) 
    print("입력된 비밀번호는 {0} 입니다".format(password))
    firstpassword.delete("1.0",END)
    
btn = Button(root, text="확인",command = cmd2)
btn.pack()

label2 = Label(root, text="비밀번호를 입력하세요")
label2.pack()

def cmd1():
    if password == (enterpassword.get("1.0",END)):
        lable.config(image=img1)  
    else :
        print("비밀번호가 틀렸습니다") 
        lable.config(image=img2)    
    enterpassword.delete("1.0",END)

enterpassword = Text(root,width=20,height=7)
enterpassword.pack()

btn = Button(root, text="확인",command = cmd1)
btn.pack()

lable = Label(root,image=img)
lable.pack()

root.mainloop()

