class Payment:


    def __init__(self, payment_id, cardholder_name, card_number, date_of_expiry):
        self.__payment_id = payment_id
        self.__cardholder_name = cardholder_name
        self.__card_number = card_number
        self.__date_of_expiry = date_of_expiry


    def get_payment_id(self):
        return self.__payment_id

    def get_cardholder_name(self):
        return self.__cardholder_name

    def get_card_number(self):
        return self.__card_number

    def get_date_of_expiry(self):
        return self.__date_of_expiry



    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    def set_cardholder_name(self, cardholder_name):
        self.__cardholder_name = cardholder_name

    def set_card_number(self, card_number):
        self.__card_number = card_number

    def set_date_of_expiry(self, date_of_expiry):
        self.__date_of_expiry = date_of_expiry


