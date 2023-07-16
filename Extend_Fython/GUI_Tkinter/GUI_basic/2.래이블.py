from tkinter import*

root = Tk()
root.title("단리복리계산기 입니다")
root.geometry("640x480")

원금입력요구창 = Label(root,text="원금(만원)을 입력하세요")
원금입력요구창.pack()

이자율입력요구창 = Label(root,text="이자율(%)을 입력하세요")
이자율입력요구창.pack()

기간입력요구창 = Label(root, text="기간(년)을 입력하세요")
기간입력요구창.pack()

단리복리 = Label(root,text="단리,복리를 선택하세요")
단리복리.pack()


root.mainloop()
