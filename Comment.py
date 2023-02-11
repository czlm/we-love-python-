class Comment:
    count_id = 0

    def __init__(self, name, number, email, enquiry):
        Comment.count_id += 1
        self._cmt_id = Comment.count_id
        self._name = name
        self._number = number
        self._email = email
        self._enquiry = enquiry

    def get_cmt_id(self):
        return self._cmt_id
    def get_name(self):
        return self._name
    def get_number(self):
        return self._number
    def get_email(self):
        return self._email
    def get_enquiry(self):
        return self._enquiry

    def set_cmt_id(self, cmt_id):
        self._cmt_id = cmt_id
    def set_name(self, name):
        self._name = name
    def set_number(self, number):
        self._number = number
    def set_email(self, email):
        self._email = email
    def set_enquiry(self, enquiry):
        self._enquiry = enquiry
