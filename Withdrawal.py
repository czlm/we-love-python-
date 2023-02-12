class Withdrawal:
    def __init__(self, withdrawal_id, first_name, last_name,level,  subject ,reason, feedback,ack):
        self.__withdrawal_id = withdrawal_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__subject = subject
        self.__level = level
        self.__feedback = feedback
        self.__reason = reason
        self.__ack = ack


    def get_withdrawal_id(self):
        return self.__withdrawal_id
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_level(self):
        return self.__level
    def get_subject(self):
        return self.__subject
    def get_feedback(self):
        return self.__feedback
    def get_reason(self):
        return self.__reason
    def get_ack(self):
        return self.__ack
    def set_withdrawal_id(self, withdrawal_id):
        self.__withdrawal_id = withdrawal_id
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def set_last_name(self, last_name):
        self.__last_name= last_name
    def set_level(self, level):
        self.__level = level
    def set_subject(self, subject):
        self.__subject = subject

    def set_reason(self, reason):
        self.__reason = reason
    def set_feedback(self, feedback):
        self.__feedback = feedback
    def set_ack(self, tof):
        self.__ack = tof
