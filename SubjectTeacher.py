class SubjectTeacher:
    def __init__(self, subject_teacher_id, subject_id, teacher_id):
        self.__subject_teacher_id = subject_teacher_id
        self.__subject_id = subject_id
        self.__teacher_id = teacher_id


    def get_subject_teacher_id(self):
        return self.__subject_teacher_id

    def get_teacher_id(self):
        return self.__teacher_id

    def get_subject_id(self):
        return  self.__subject_id



    def set_subject_teacher_id(self, subject_teacher_id):
        self.__subject_teacher_id = subject_teacher_id

    def set_teacher_id(self, teacher_id):
        self.__teacher_id = teacher_id

    def set_subject_id(self,subject_id):
        self.__subject_id = subject_id

