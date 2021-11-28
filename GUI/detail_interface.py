from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from PIL import ImageTk,Image

class DetailGUI(Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("600x600+70+150")
        self.resizable(0,0)
        self.style02 = Style()
        self.style02.configure("Title.TLabel",font=("微软雅黑",20,"bold"),foreground="Black",background="lightblue")
        self.style02.configure("TPanedwindow",background="LightBlue")
        self.style02.configure("TButton",font=("微软雅黑",9),foreground="Black",background="lightgray")
        # 设置主框样式
        self.iconbitmap("E:\Project\Object_Oriented\综合案例演示\File\school.ico")
        # 设置界面样式
        self.login_image = ImageTk.PhotoImage(Image.open("E:\Project\Object_Oriented\综合案例演示\File\图片.gif").resize((600,100),Image.ANTIALIAS))
        self.label_image = Label(self,image=self.login_image)
        self.label_image.place(x=0,y=0)
        self.label_title = Label(self,text="",style="Title.TLabel")
        self.label_title.place(x=180,y=20)
        self.pane_detail = Panedwindow(self,width=590,height=420,style="TPanedwindow")
        self.pane_detail.place(x=5,y=105)
        self.button_detail01 = Button(self,text="关闭",style="TButton",width=10,command=self.close_student_detail)
        self.button_detail01.place(x=515,y=525)
        self.button_detail02 = Button(self, text="保存",style="TButton",width=10,command=self.commit)
        self.button_detail02.place(x=435, y=525)
    def close_student_detail(self):
        self.destroy()
    def commit(self):
        pass
if __name__ == "__main__":
    detail = DetailGUI()
    detail.mainloop()