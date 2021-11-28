from check import *
from service import *
from main_interface import *
from studentdetail import *
from person import *

class StudentService(Service,Check):
    def __init__(self,list_all:list,current_student:Student):
        Check.__init__(self)
        Service.__init__(self)
        self.list_all = list_all
        self.current_student = current_student
    def check(self):
        num = 0
        if not self.check_sno(self.current_student.sno):
            num = 2
        elif not self.check_name(self.current_student.name):
            num = 3
        elif not self.check_phone(self.current_student.phone):
            num = 4
        elif not self.check_email(self.current_student.email):
            num = 5
        else:
            num = 1
        return num

    def add(self):
        current_student_list = []
        current_student_list.append(self.current_student.sno)
        current_student_list.append(self.current_student.name)
        current_student_list.append(self.current_student.gender)
        current_student_list.append(self.current_student.birthday)
        current_student_list.append(self.current_student.phone)
        current_student_list.append(self.current_student.major)
        current_student_list.append(self.current_student.study_time)
        self.list_all.append(current_student_list)

    def update(self):
        for index in range(len(self.list_all)):
            if self.list_all[index][0] == self.current_student.sno:
                self.list_all[index][1] == self.current_student.name
                self.list_all[index][2] == self.current_student.gender
                self.list_all[index][3] == self.current_student.birthday
                self.list_all[index][4] == self.current_student.phone
                self.list_all[index][5] == self.current_student.email
                self.list_all[index][6] == self.current_student.major
                self.list_all[index][7] == self.current_student.study_time
    def delete(self):
        pass