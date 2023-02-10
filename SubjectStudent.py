class SubjectStudent:
    def __init__(self, subject_student_id, subject_id, student_id):
        self.__subject_student_id = subject_student_id
        self.__subject_id = subject_id
        self.__student_id = student_id

    def get_subject_student_id(self):
        return self.__subject_student_id

    def get_student_id(self):
        return self.__student_id

    def get_subject_id(self):
        return  self.__subject_id

    def set_subject_student_id(self, subject_student_id):
        self.__subject_student_id = subject_student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_subject_id(self,subject_id):
        self.__subject_id = subject_id
