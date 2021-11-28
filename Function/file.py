import os

class File:
    def __init__(self):
        self.Student_path = "E:\Project\Object_Oriented\综合案例演示\File\Student.txt"
        self.Teacher_path = "E:\Project\Object_Oriented\综合案例演示\File\Teacher.txt"
        self.student_list_all = []
        self.teacher_list_all = []
        self.read_from_file()

    def read_from_file(self):
        try:
            with open(self.Student_path,mode="r",encoding="utf-8") as f:
                current_line = f.readline()
                while current_line:
                    student_list = current_line.split(",")
                    self.student_list_all.append(student_list)
                    current_line = f.readline()
        except Exception as e:
            raise e
        try:
            with open(self.Teacher_path,mode="r",encoding="utf-8") as f:
                current_line = f.readline()
                while current_line:
                    teacher_list = current_line.split(",")
                    self.teacher_list_all.append(teacher_list)
                    current_line = f.readline()
        except Exception as e:
            raise e