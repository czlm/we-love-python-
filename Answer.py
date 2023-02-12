from Student import *

class Answer:
    def __init__(self, answer_id, student_id, subject_id, a1, a2, a3, a4, a5):
        self.__answer_id = answer_id
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__a5 = a5
        self.__student_id = student_id
        self.__subject_id = subject_id

    def get_answer_id(self):
        return self.__answer_id
    def get_student_id(self):
        return self.__student_id
    def get_subject_id(self):
        return self.__subject_id
    def get_a1(self):
        return self.__a1
    def get_a2(self):
        return self.__a2
    def get_a3(self):
        return self.__a3
    def get_a4(self):
        return self.__a4
    def get_a5(self):
        return self.__a5

    def set_answer_id(self, answer_id):
        self.__answer_id = answer_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_subject_id(self, subject_id):
        self.__subject_id = subject_id

    def set_a1(self,a1):
        self.__a1 = a1

    def set_a2(self,a2):
        self.__a2 = a2

    def set_a3(self,a3):
        self.__a3 = a3

    def set_a4(self,a4):
        self.__a4 = a4

    def set_a5(self,a5):
        self.__a5 = a5