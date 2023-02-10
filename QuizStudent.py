class QuizStudent:
    def __init__(self, quiz_student_id, quiz_id, student_id, attempt_id):
        self.__quiz_student_id = quiz_student_id
        self.__quiz_id = quiz_id
        self.__student_id = student_id
        self.__attempt_id = attempt_id

    def get_quiz_student_id(self):
        return self.__quiz_student_id

    def get_quiz_id(self):
        return self.__quiz_id

    def get_student_id(self):
        return self.__student_id

    def get_attempt_id(self):
        return self.__attempt_id

    def set_quiz_student_id(self, quiz_student_id):
        self.__quiz_student_id = quiz_student_id

    def set_quiz_id(self, quiz_id):
        self.__quiz_id = quiz_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_attempt_id(self, attempt_id):
        self.__attempt_id = attempt_id