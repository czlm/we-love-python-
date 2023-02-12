class Grade:

    def __init__(self, grade_id, first_name, last_name, topic_no, topic_title, percentage, grade, user_id):
        self.__grade_id = grade_id
        self.__first_name = first_name
        self.__last_name = last_name
        # self.__day = day
        # self.__start_time = start_time
        # self.__end_time = end_time
        self.__topic_no = topic_no
        self.__topic_title = topic_title
        self.__percentage = percentage
        self.__grade = grade
        self.__user_id = user_id

    def set_grade_id(self, grade_id):
        self.__grade_id = grade_id

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

    def set_topic_no(self, topic_no):
        self.__topic_no = topic_no

    def set_topic_title(self, topic_title):
        self.__topic_title = topic_title

    def set_percentage(self, percentage):
        self.__percentage = percentage

    def set_grade(self, grade):
        self.__grade = grade

    def set_user_id(self, user_id):
        self.__user_id = user_id


    def get_grade_id(self):
        return self.__grade_id

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

    def get_topic_no(self):
        return self.__topic_no

    def get_topic_title(self):
        return self.__topic_title

    def get_percentage(self):
        return self.__percentage

    def get_grade(self):
        return self.__grade
