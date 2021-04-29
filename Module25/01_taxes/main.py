
class Property:

    def __init__(self, worth):
        self.worth = worth

    def tax_calculation(self, tax):
        res_tax = self.worth * (tax / 100)
        return  res_tax

class Appartment(Property):

    # TODO, предлагаю сумму налога tax переопределять в методе init =)
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self, tax = 1000):
        return self.worth / tax

class Car(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self, tax = 200):
        return self.worth / tax


class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self, tax = 500):
        return self.worth / tax

print("Для рассчета налога - введите количество денег и стоимость имущества: ")
bank = int(input("Количество денег: "))
car_price = int(input("Стоимость машины: "))
appartament_price = int(input("Стоимость аппартаментов: "))
house_price = int(input("Стоимость дачи: "))
car = Car(car_price)
appartament = Appartment(appartament_price)
house =CountryHouse(house_price)

if bank >= car.tax_calculation() + appartament.tax_calculation() + house.tax_calculation():
    print("Для оплаты транспортного налога {}, налога на аппартменты {}, налога на дачу {} у Вас достаточно средств".format(
        car.tax_calculation(), appartament.tax_calculation(), house.tax_calculation()
    ))
else:
    credit = bank - car.tax_calculation() - appartament.tax_calculation() - house.tax_calculation()
    print("Для оплаты транспортного налога {}, налога на аппартменты {}, налога на дачу {} у Вас недостаточно средств".format(
        car.tax_calculation(), appartament.tax_calculation(), house.tax_calculation()
    ))
    print("Что бы оплатить нужно еще денег: {}".format(abs(credit)))