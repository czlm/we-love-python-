from Level import *
class Subject(Level):

    def __init__(self, subject_id, title, description,price, level_id):
        super().__init__(level_id)
        self.__level_id = level_id
        self.__subject_id = subject_id
        self.__title = title
        self.__description = description
        self.__price = price

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_subject_id(self):
        return self.__subject_id

    def get_price(self):
        return self.__price


    def set_description(self, description):
        self.__description = description

    def set_title(self, title):
        self.__title = title

    def set_subject_id(self, id):
        self.__subject_id = id

    def set_price(self, price):
        self.__price = price
