class Person:
    def __init__(self,name,gender,birthday,phone,email):
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.phone = phone
        self.email = email

class Student(Person):
    def __init__(self,sno,name,gender,birthday,phone,email,major,study_time):
        super().__init__(name,gender,birthday,phone,email)
        self.sno = sno
        self.major = major
        self.study_time = study_time

class Teacher(Person):
    def __init__(self,tid,name,gender,birthday,phone,email,professional,college,induction):
        super().__init__()
        self.tid = tid
        self.professional = professional
        self.college = college
        self.induction = induction