
class Quiz:
    def __init__(self, teacher_id, subject_id, quiz_id, student_id, title, description,q1,q2,q3,q4,q5,a1,a2,a3,a4,a5, ms1,ms2,ms3,ms4,ms5,s1,s2,s3,s4,s5,r1,r2,r3,r4,r5, as1, status):
        self.__teacher_id = teacher_id
        self.__subject_id = subject_id
        self.__quiz_id = quiz_id
        self.__student_id = student_id
        self.__title = title
        self.__description = description
        self.__q1 = q1
        self.__q2 = q2
        self.__q3 = q3
        self.__q4 = q4
        self.__q5 = q5
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__a5 = a5
        self.__ms1 = ms1
        self.__ms2 = ms2
        self.__ms3 = ms3
        self.__ms4 = ms4
        self.__ms5 = ms5
        self.__s1 = s1
        self.__s2 = s2
        self.__s3 = s3
        self.__s4 = s4
        self.__s5 = s5
        self.__r1 = r1
        self.__r2 = r2
        self.__r3 = r3
        self.__r4 = r4
        self.__r5 = r5
        self.__as1 = as1
        self.__status = status

    def get_teacher_id(self):
        return self.__teacher_id

    def get_subject_id(self):
        return self.__subject_id

    def get_quiz_id(self):
        return self.__quiz_id

    def get_student_id(self):
        return self.__student_id

    def get_q1(self):
        return self.__q1
    def get_q2(self):
        return self.__q2
    def get_q3(self):
        return self.__q3
    def get_q4(self):
        return self.__q4
    def get_q5(self):
        return self.__q5

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

    def get_ms1(self):
        return self.__ms1

    def get_ms2(self):
        return self.__ms2

    def get_ms3(self):
        return self.__ms3

    def get_ms4(self):
        return self.__ms4

    def get_ms5(self):
        return self.__ms5

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

    def get_r1(self):
        return self.__r1

    def get_r2(self):
        return self.__r2

    def get_r3(self):
        return self.__r3

    def get_r4(self):
        return self.__r4

    def get_r5(self):
        return self.__r5
    def get_as1(self):
        return self.__as1
    def get_status(self):
        return self.__as1

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description
    def set_title(self, title):
        self.__title = title

    def set_description(self, description):
        self.__description = description


    def set_teacher_id(self, teacher_id):
        self.__teacher_id = teacher_id

    def set_subject_id(self, subject_id):
        self.__subject_id = subject_id

    def set_quiz_id(self, quiz_id):
        self.__quiz_id = quiz_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_q1(self, q1):
        self.__q1 = q1

    def set_q2(self, q2):
        self.__q2 =  q2

    def set_q3(self,q3):
        self.__q3 = q3

    def set_q4(self,q4):
        self.__q4 = q4

    def set_q5(self, q5):
        self.__q5 = q5

    def set_a1(self, a1):
        self.__a1 = a1

    def set_a2(self,a2):
        self.__a2 = a2

    def set_a3(self, a3):
        self.__a3 = a3

    def set_a4(self,a4):
        self.__a4 = a4

    def set_a5(self, a5):
        self.__a5 = a5

    def set_ms1(self, ms1):
        self.__ms1 = ms1

    def set_ms2(self, ms2):
        self.__ms2 = ms2

    def set_ms3(self, ms3):
        self.__ms3 = ms3

    def set_ms4(self, ms4):
        self.__ms4 = ms4

    def set_ms5(self, ms5):
        self.__ms5 = ms5

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

    def set_r1(self, r1):
        self.__r1 =r1

    def set_r2(self, r2):
        self.__r2 = r2

    def set_r3(self, r3):
        self.__r3 = r3

    def set_r4(self, r4):
        self.__r4 = r4

    def set_r5(self, r5):
        self.__r5 = r5

    def set_as1(self, as1):
        self.__as1 = as1

    def set_status(self, status):
        self.__status = status

