from datetime import date


class PayRollDeduction:
    def __init__(self,description,date,charge_amt,id):
        self.__desc=description
        self.__date=date
        self.__chrg=charge_amt
        self.__id=id
    def get_desc(self):
        return self.__desc
    def get_date(self):
        return self.__date
    def get_chrg(self):
        return self.__chrg
    def get_id(self):
        return self.__id
    