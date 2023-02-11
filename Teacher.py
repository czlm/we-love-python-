class Teacher:
    count_id = 0

    def __init__(self, teacher_id, first_name, last_name, gender, email, date_joined, address, subject):
        self.__teacher_id = teacher_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__email = email
        self.__date_joined = date_joined
        self.__address = address
        self.__subject = subject


    def get_teacher_id(self):
        return self.__teacher_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def get_email(self):
        return self.__email

    def get_date_joined(self):
        return self.__date_joined

    def get_address(self):
        return self.__address

    def set_subject(self, subject):
        self.__subject = subject


    def set_teacher_id(self, teacher_id):
        self.__teacher_id = teacher_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_gender(self, gender):
        self.__gender = gender

    def set_email(self, email):
        self.__email = email

    def set_date_joined(self, date_joined):
        self.__date_joined = date_joined

    def set_address(self, address):
        self.__address = address

    def get_subject(self):
        return self.__subject
