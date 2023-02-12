class Content:

    def __init__(self, content_id, title, content):
        self.__content_id = content_id
        self.__title = title
        self.__content = content


    def set_grade_id(self, grade_id):
        self.__grade_id = grade_id

    def set_title(self, title):
        self.__title = title

    def set_content(self, content):
        self.__content = content


    def get_content_id(self):
        return self.__content_id

    def get_title(self):
        return self.__title

    def get_content(self):
        return self.__content
