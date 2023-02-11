class FAQ:
    count_id = 0

    def __init__(self, question, answer):
        FAQ.count_id += 1
        self._faq_id = FAQ.count_id
        self._question = question
        self._answer = answer

    def get_faq_id(self):
        return self._faq_id
    def get_question(self):
        return self._question
    def get_answer(self):
        return self._answer

    def set_faq_id(self, faq_id):
        self._faq_id = faq_id
    def set_question(self, question):
        self._question = question
    def set_answer(self, answer):
        self._answer = answer
