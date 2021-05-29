import datetime


class Date:
    # TODO, предлагаю сделать 3 параметра. День, месяц и год, вместо одного =)
    def __init__(self, date_string: str):
        self.date_string = date_string

    # TODO, стоит добавить метод __str__ и возвращать дату в удобном формате =)

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
        # TODO, стоит добавить возврат себя с нужными данными, которые мы передаём в init. =)
        #  Если поправить init, то нужно будет разбить дату на 3 параметра и предавать их при возврате себя.


date = Date.date_from_string(date_string="10-12-2016")
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))