class Level:
    def __init__(self, level_id):
        self.__level_id = level_id

    def get_level_id(self):
        return self.__level_id

    def set_level_id(self, level_id):
        self.__level_id = level_id