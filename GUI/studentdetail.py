from detail_interface import *
from tkinter.messagebox import *
from person import *
from studentservice import *

class StudentDetail(DetailGUI):
    def __init__(self,flag,list_student_all:list,current_student:list):
        super().__init__()
        self.flag = flag
        self.current_student = current_student
        self.list_student_all = list_student_all
        self.label_title["text"] = "学生基本信息明细"
        self.style02.configure("TLabel",font=("微软雅黑",12),foreground="Navy")
        self.style02.configure("TRadiobutton",font=("微软雅黑",10))
        self.setup_student_detail()
        self.load_gui_student_detail()

    def setup_student_detail(self):
        self.label_sno = Label(self.pane_detail,text="学号：")
        self.label_sno.place(x=135,y=20)
        self.var_sno = StringVar()
        self.entry_sno = Entry(self.pane_detail,textvariable=self.var_sno,font=("微软雅黑",12),background="black",width=20)
        self.entry_sno.place(x=188,y=19)

        self.label_name = Label(self.pane_detail, text="姓名：")
        self.label_name.place(x=135, y=50)
        self.var_name = StringVar()
        self.entry_name = Entry(self.pane_detail,textvariable=self.var_name, font=("微软雅黑", 12), background="black", width=20)
        self.entry_name.place(x=188, y=49)

        self.label_gender = Label(self.pane_detail, text="性别：")
        self.label_gender.place(x=135, y=80)
        self.var_gender = IntVar()
        self.Radio_men = Radiobutton(self.pane_detail,text="男",variable=self.var_gender,value=1)
        self.Radio_men.place(x=188, y=80)
        self.Radio_women = Radiobutton(self.pane_detail, text="女", variable=self.var_gender, value=2)
        self.Radio_women.place(x=224, y=80)

        self.label_birthday = Label(self.pane_detail, text="出生日期：")
        self.label_birthday.place(x=103, y=110)
        self.var_birthday = StringVar()
        self.entry_birthday = Entry(self.pane_detail,textvariable=self.var_birthday, font=("微软雅黑", 12), background="black", width=20)
        self.entry_birthday.place(x=188, y=109)

        self.label_phone = Label(self.pane_detail, text="电话号码：")
        self.label_phone.place(x=103, y=140)
        self.var_phone = StringVar()
        self.entry_phone = Entry(self.pane_detail,textvariable=self.var_phone, font=("微软雅黑", 12), background="black", width=20)
        self.entry_phone.place(x=188, y=139)

        self.label_email = Label(self.pane_detail, text="邮箱地址：")
        self.label_email.place(x=103, y=170)
        self.var_email = StringVar()
        self.entry_email = Entry(self.pane_detail, textvariable=self.var_email,font=("微软雅黑", 12), background="black", width=20)
        self.entry_email.place(x=188, y=169)

        self.label_major = Label(self.pane_detail, text="所学专业：")
        self.label_major.place(x=103, y=200)
        self.var_major = StringVar()
        self.entry_major = Entry(self.pane_detail,textvariable=self.var_major, font=("微软雅黑", 12), background="black", width=20)
        self.entry_major.place(x=188, y=199)

        self.label_study_time = Label(self.pane_detail, text="入学时间：")
        self.label_study_time.place(x=103, y=230)
        self.var_study_time = StringVar()
        self.entry_study_time = Entry(self.pane_detail, textvariable=self.var_study_time,font=("微软雅黑", 12), background="black", width=20)
        self.entry_study_time.place(x=188, y=229)

    def load_gui_student_detail(self):
        if self.flag == 1:
            self.label_title["text"] = "查看学生明细"
            self.button_detail02.place_forget()
            self.var_sno.set(self.current_student[0])
            self.var_name.set(self.current_student[1])
            if "男" in self.current_student[2]:
                self.var_gender.set(1)
            else:
                self.var_gender.set(2)
            self.var_birthday.set(self.current_student[3])
            self.var_phone.set(self.current_student[4])
            self.var_email.set(self.current_student[5])
            self.var_major.set(self.current_student[6])
            self.var_study_time.set(self.current_student[7])

            self.entry_sno["state"] = DISABLED
            self.entry_name["state"] = DISABLED
            self.Radio_men["state"] = DISABLED
            self.Radio_women["state"] = DISABLED
            self.entry_phone["state"] = DISABLED
            self.entry_email["state"] = DISABLED
            self.entry_major["state"] = DISABLED
            self.entry_study_time["state"] = DISABLED
            self.entry_birthday["state"] = DISABLED

        elif self.flag == 2:
            self.label_title["text"] = "添加学生明细"

        elif self.flag == 3:
            self.label_title["text"] = "修改学生明细"
            self.var_sno.set(self.current_student[0])

    def commit(self):
        super().commit()
        if self.flag == 2:
            current_student = self.get_current_student()
            student_service = StudentService(self.list_student_all,current_student)
            return_num = student_service.check()
            if return_num == 2:
                showinfo("系统消息","学号不符合要求:请输入六位的数字")
            elif return_num == 3:
                showinfo("系统消息","姓名不符合要求:请输入二到四位的汉字")
            elif return_num == 4:
                showinfo("系统消息","电话号码不符合要求:请输入规范的11位数字")
            elif return_num == 5:
                showinfo("系统消息","邮箱格式不符合要求:请输入规范的邮箱")
            elif return_num == 1:
                showinfo("系统消息","符合要求")
                student_service.add()
                self.student_id = 1
            self.destroy()

    def get_current_student(self):
        sno = self.var_sno.get()
        name = self.var_name.get()
        if self.var_gender.get() == 1:
            gender = "男"
        elif self.var_gender.get() == 2:
            gender = "女"
        birthday = self.var_birthday.get()
        phone = self.var_phone.get()
        email = self.var_email.get()
        major = self.var_major.get()
        study_time = self.var_study_time.get()
        current_student = Student(sno,name,gender,birthday,phone,email,major,study_time)
        return current_student

if __name__ == "__main__":
    student = StudentDetail()
    student.mainloop()