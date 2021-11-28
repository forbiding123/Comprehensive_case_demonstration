"""
实现输入规范check类，规范如下：
1.学号95开头的9位数字
2.姓名4个以内的汉字
3.性别只能填写“男”或“女"
4.手机号码符合基本规范
5.邮箱地址符合基本规范
"""

import re
from person import *

class Check:
    def check_sno(self,sno):
        reg = re.compile("^95\d{4}$")
        result = reg.match(sno)
        if result is None:
            return False
        else:
            return True
    def check_name(self, name:str):
        if 1 < len(name) <= 4:
            for item in name:
                if item < "\u4E00" and item > "\u9FA5":
                    return False
            return True
        else:
            return False
    def check_gender(self, gender:str):
        if gender.strip() in ["男", "女"]:
            return True
        else:
            return False
    def check_phone(self, phone):
        reg = re.compile("^[1][3578]\d{9}$")
        result = reg.match(phone)
        if result is None:
            return False
        else:
            return True
    def check_email(self, email):
        reg = re.compile("\w{1,}[@]\w{1,}[.]\w{1,}")
        result = reg.match(email)
        if result is None:
            return False
        else:
            return True
