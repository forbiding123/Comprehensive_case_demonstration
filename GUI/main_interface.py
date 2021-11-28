from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from file import *
from studentdetail import *

class MainGui(Tk):
    def __init__(self):
        super().__init__()
        self.title("学生教师基本信息")
        self.geometry("1200x600+100+100")
        self.resizable(0,0)
        self.style = Style()
        self.style.configure("Main.TLabel",font=("微软雅黑",12,"bold"),foreground="black",background="lightblue")
        self.label_student = Label(self,text="学生信息：",style="Main.TLabel")
        self.label_student.place(x=10,y=20)
        self.label_teacher = Label(self, text="教师信息：",style="Main.TLabel")
        self.label_teacher.place(x=580,y=20)
        self.setUI_student()
        self.setUI_teacher()
        self.file_info = File()
        self.student_all = self.file_info.student_list_all
        self.teacher_all = self.file_info.teacher_list_all
        self.student_current = []
        self.flag = 0
        self.load_student()
        self.load_teacher()
        self.Tree_student.bind("<Double-1>",self.view_student_select)
    def setUI_student(self):
        self.Tree_student = Treeview(self, columns=("sno","name","gender","major","phone","email"),show="headings",height=22)
        self.Tree_student.column("sno",width=90,anchor="center")
        self.Tree_student.column("name", width=80, anchor="center")
        self.Tree_student.column("gender", width=40, anchor="center")
        self.Tree_student.column("major", width=100, anchor="center")
        self.Tree_student.column("phone", width=120, anchor="center")
        self.Tree_student.column("email", width=120, anchor="center")
        self.Tree_student.heading("sno", text="学号")
        self.Tree_student.heading("name", text="姓名")
        self.Tree_student.heading("gender", text="性别")
        self.Tree_student.heading("major", text="专业")
        self.Tree_student.heading("phone", text="电话号码")
        self.Tree_student.heading("email", text="邮箱")
        self.Tree_student.place(x=10,y=60)
        self.button_student_delete = Button(self,text="添加",command=self.view_student_add)
        self.button_student_delete.place(x=306,y=530)
        self.button_student_update = Button(self, text="修改",command = self.view_student_update)
        self.button_student_update.place(x=392, y=530)
        self.button_student_add = Button(self, text="删除")
        self.button_student_add.place(x=478, y=530)
    def setUI_teacher(self):
        self.Tree_teacher = Treeview(self, columns=("tid", "name", "gender", "title", "college","phone"),
                                     show="headings", height=22)
        self.Tree_teacher.column("tid", width=90, anchor="center"),
        self.Tree_teacher.column("name", width=80, anchor="center")
        self.Tree_teacher.column("gender", width=40, anchor="center")
        self.Tree_teacher.column("title", width=120, anchor="center")
        self.Tree_teacher.column("college", width=140, anchor="center")
        self.Tree_teacher.column("phone", width=140, anchor="center")
        self.Tree_teacher.heading("tid", text="编号")
        self.Tree_teacher.heading("name", text="姓名")
        self.Tree_teacher.heading("gender", text="性别")
        self.Tree_teacher.heading("title", text="职称")
        self.Tree_teacher.heading("college", text="毕业院校")
        self.Tree_teacher.heading("phone", text="手机号码")
        self.Tree_teacher.place(x=580, y=60)
        self.button_teacher_delete = Button(self, text="添加")
        self.button_teacher_delete.place(x=936, y=530)
        self.button_teacher_update = Button(self, text="修改")
        self.button_teacher_update.place(x=1022, y=530)
        self.button_teacher_add = Button(self, text="修改")
        self.button_teacher_add.place(x=1108, y=530)
    def load_student(self):
        for index in self.Tree_student.get_children():
            self.Tree_student.delete(index)
        if len(self.student_all) == 0:
            showinfo("系统消息","没有任何信息进行加载")
        else:
            for index in range(len(self.student_all)):
                self.Tree_student.insert("",index,values=
                (self.student_all[index][0],self.student_all[index][1],self.student_all[index][2],
                 self.student_all[index][6],self.student_all[index][4],self.student_all[index][5],))
    def load_teacher(self):
        for index in self.Tree_teacher.get_children():
            self.Tree_teacher.delete(index)
        if len(self.teacher_all) == 0:
            showinfo("系统消息","没有任何信息进行加载")
        else:
            for index in range(len(self.teacher_all)):
                self.Tree_teacher.insert("",index,values=
                (self.teacher_all[index][0],self.teacher_all[index][1],self.teacher_all[index][2],
                 self.teacher_all[index][6],self.teacher_all[index][7],self.teacher_all[index][4],))
    def view_student_select(self,event):
        item = self.Tree_student.selection()
        current_student = self.Tree_student.item(item,"values")
        for item in self.student_all:
            if current_student[0] == item[0]:
                self.student_current = item
        self.flag = 1
        student_select = StudentDetail(self.flag,self.student_all,self.student_current)
    def view_student_add(self):
        self.flag = 2
        student_add = StudentDetail(self.flag,self.student_all,self.student_current)
        self.wait_window(student_add)
        num = student_add.student_id
        if num == 1:
            self.load_student()
    def view_student_update(self):
        student_update = StudentDetail(3)


if __name__  == "__main__":
    main = MainGui()
    main.mainloop()