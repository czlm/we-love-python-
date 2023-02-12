class User:
    count_id = 0

    # initializer method
    def __init__(self, name, phonenumber, name1, phonenumber1):
        User.count_id += 1
        self.__user_id = User.count_id
        self.__name = name
        self.__phonenumber = phonenumber
        self.__name1 = name1
        self.__phonenumber1 = phonenumber1

    # accessor methods
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_phonenumber(self):
        return self.__phonenumber

    def get_name1(self):
        return self.__name1

    def get_phonenumber1(self):
        return self.__phonenumber1


    # mutator methods
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_name(self, name):
        self.__name = name

    def set_phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber

    def set_name1(self, name1):
        self.__name1 = name1

    def set_phonenumber1(self, phonenumber1):
        self.__phonenumber1 = phonenumber1
