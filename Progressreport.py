class Progressreport:

    def __init__(self, progressreport_id, first_name, last_name, comments, overall_ratings, user_id):
        self.__progressreport_id = progressreport_id
        self.__first_name = first_name
        self.__last_name = last_name
        # self.__day = day
        # self.__start_time = start_time
        # self.__end_time = end_time
        self.__comments = comments
        self.__overall_ratings = overall_ratings
        self.__user_id = user_id


    def set_progressreport_id(self, progressreport_id):
        self.__progressreport_id = progressreport_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    # def set_day(self, day):
    #     self.__day = day
    #
    # def set_start_time(self, start_time):
    #     self.__start_time = start_time
    #
    # def set_end_time(self, end_time):
    #     self.__end_time = end_time

    def set_comments(self, comments):
        self.__comments = comments

    def set_overall_ratings(self, overall_ratings):
        self.__overall_ratings = overall_ratings

    def set_user_id(self, user_id):
        self.__user_id = user_id


    def get_progressreport_id(self):
        return self.__progressreport_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    # def get_day(self):
    #     return self.__day
    #
    # def get_start_time(self):
    #     return self.__start_time
    #
    # def get_end_time(self):
    #     return self.__end_time

    def get_comments(self):
        return self.__comments

    def get_overall_ratings(self):
        return self.__overall_ratings

    def get_user_id(self):
        return self.__user_id
