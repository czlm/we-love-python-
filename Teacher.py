
class Teacher:

    def __init__(self, first_name, last_name, gender, teacher_id, email, date_joined, address, subject1, subject2, subject3, subject4):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__teacher_id = teacher_id
        self.__email = email
        self.__date_joined = date_joined
        self.__address = address
        self.__subject1 = subject1
        self.__subject2 = subject2
        self.__subject3 = subject3
        self.__subject4 = subject4

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def get_teacher_id(self):
        return self.__teacher_id

    def get_email(self):
        return self.__email

    def get_date_joined(self):
        return self.__date_joined

    def get_address(self):
        return self.__address

    def get_subejct1(self):
        return self.__subject1
    def get_subejct2(self):
        return self.__subject2
    def get_subejct3(self):
        return self.__subject3
    def get_subejct4(self):
        return self.__subject4

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_gender(self, gender):
        self.__gender = gender

    def set_teacher_id(self, teacher_id):
        self.__teacher_id = teacher_id

    def set_email(self, email):
        self.__email = email

    def set_date_joined(self, date_joined):
        self.__date_joined = date_joined

    def set_address(self, address):
        self.__address = address

    def set_subejct1(self, subject1):
       self.__subject1 = subject1
    def set_subejct2(self, subject2):
        self.__subject2 = subject2
    def set_subejct3(self, subject3):
        self.__subject3 = subject3
    def set_subejct4(self, subject4):
        self.__subject4 = subject4
