class Property:

    def __init__(self, worth):
        self.worth = worth

    def tax_calculation(self, tax):
        res_tax = self.worth * (tax / 100)
        return res_tax


class Appartment(Property):

    # , предлагаю сумму налога tax переопределять в методе init =)
    def __init__(self, worth):
        super().__init__(worth)
        self.tax = worth / 1000
        # TODO, 1000 и worth стоит реализовать аргументами класса.
        #  А расчёт налога, возможно, лучше сделать отдельным методом.


class Car(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.tax = worth / 200


class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.tax = worth / 500


print("Для рассчета налога - введите количество денег и стоимость имущества: ")
bank = int(input("Количество денег: "))
car_price = int(input("Стоимость машины: "))
appartament_price = int(input("Стоимость аппартаментов: "))
house_price = int(input("Стоимость дачи: "))
car = Car(car_price)
appartament = Appartment(appartament_price)
house = CountryHouse(house_price)

if bank >= car.tax + appartament.tax + house.tax:
    print(
        "Для оплаты транспортного налога {}, налога на аппартменты {}, налога на дачу {} у Вас достаточно средств".format(
            car.tax, appartament.tax, house.tax
        ))
else:
    credit = bank - car.tax - appartament.tax - house.tax
    print(
        "Для оплаты транспортного налога {}, налога на аппартменты {}, налога на дачу {} у Вас недостаточно средств".format(
            car.tax, appartament.tax, house.tax
        ))
    print("Что бы оплатить нужно еще денег: {}".format(abs(credit)))
