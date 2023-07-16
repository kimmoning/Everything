from tkinter import*

root = Tk()

Photo = PhotoImage(file="GUI_basic/img.png")
photo2 = PhotoImage(file="GUI_basic/img2.png")

root.title("한번누르를 때마다 이미지가 바뀌어요")
def cmd1():
    global photo2
    print("응애") 
    btn1.config(text="애응")
    Label.config(image=photo2)

btn1=Button(root,text="동작하는 버튼",command=cmd1)
btn1.pack()

Label=Label(root,image=Photo)
Label.pack()

root.mainloop()









