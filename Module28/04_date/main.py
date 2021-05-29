import datetime


class Date:
    def __init__(self, date_string: str):
        self.date_string = date_string

    @classmethod
    def is_date_valid(cls, date_string: str)-> bool:
        try:
            if datetime.datetime.strptime(date_string, "%d-%m-%Y"):
                return True
        except (ValueError):
            return False

    @classmethod
    def date_from_string(cls, date_string: str)->datetime:
        res = datetime.datetime.strptime(date_string, "%d-%m-%Y")
        print(res)


date = Date.date_from_string(date_string="10-12-2016")
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))