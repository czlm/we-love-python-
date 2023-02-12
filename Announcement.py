class Announcement:

    def __init__(self, announcement_id, announcement_descriptions, salutation, tutor_full_name, created_datetime, user_id):
        self.__announcement_id = announcement_id
        # self.__day = day
        # self.__start_time = start_time
        # self.__end_time = end_time
        self.__announcement_descriptions = announcement_descriptions
        self.__salutation = salutation
        self.__tutor_full_name = tutor_full_name
        self.__created_datetime = created_datetime
        self.__user_id = user_id

    def set_announcement_id(self, announcement_id):
        self.__announcement_id = announcement_id

    # def set_day(self, day):
    #     self.__day = day
    #
    # def set_start_time(self, start_time):
    #     self.__start_time = start_time
    #
    # def set_end_time(self, end_time):
    #     self.__end_time = end_time

    def set_announcement_descriptions(self, announcement_descriptions):
        self.__announcement_descriptions = announcement_descriptions

    def set_salutation(self, salutation):
        self.__salutation = salutation

    def set_tutor_full_name(self, tutor_full_name):
        self.__tutor_full_name = tutor_full_name

    def set_created_datetime(self, created_datetime):
        self.__created_datetime = created_datetime


    def get_announcement_id(self):
        return self.__announcement_id

    # def get_day(self):
    #     return self.__day
    #
    # def get_start_time(self):
    #     return self.__start_time
    #
    # def get_end_time(self):
    #     return self.__end_time

    def get_announcement_descriptions(self):
        return self.__announcement_descriptions

    def get_salutation(self):
        return self.__salutation

    def get_tutor_full_name(self):
        return self.__tutor_full_name

    def get_created_datetime(self):
        return self.__created_datetime

    def get_user_id(self):
        return self.__user_id
