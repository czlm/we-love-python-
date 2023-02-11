class Score:
    def __init__(self, score_id, student_id, s1, s2, s3, s4, s5):
        self.__score_id = score_id
        self.__student_id = student_id
        self.__s1 = s1
        self.__s2 = s2
        self.__s3 = s3
        self.__s4 = s4
        self.__s5 = s5

    def get_score_id(self):
        return self.__score_id

    def get_student_id(self):
        return self.__student_id

    def get_s1(self):
        return self.__s1

    def get_s2(self):
        return self.__s2

    def get_s3(self):
        return self.__s3

    def get_s4(self):
        return self.__s4

    def get_s5(self):
        return self.__s5

    def set_score_id(self, score_id):
        self.__score_id = score_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_s1(self, s1):
        self.__s1 = s1

    def set_s2(self, s2):
        self.__s2 = s2

    def set_s3(self, s3):
        self.__s3 = s3

    def set_s4(self, s4):
        self.__s4 = s4

    def set_s5(self, s5):
        self.__s5 = s5


