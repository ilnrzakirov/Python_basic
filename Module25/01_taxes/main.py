class Property:

    def __init__(self, worth):
        self.worth = worth

    # , параметр tax получился лишний в данном методе =)
    def tax_calculation(self):
        res_tax = self.worth / 100
        return res_tax


class Appartment(Property):


    # , предлагаю сумму налога tax переопределять в методе init =)
    def __init__(self, worth):
        super().__init__(worth)
        self.tax = 1000

        # , 1000 и worth стоит реализовать аргументами класса.
        #  А расчёт налога, возможно, лучше сделать отдельным методом.

    def tax_calculation(self):
        res_tax = self.worth / self.tax
        return res_tax


class Car(Property):


    # , предлагаю сумму налога tax переопределять в методе init =)
    def __init__(self, worth):
        super().__init__(worth)
        self.tax = 200

    def tax_calculation(self):
        res_tax = self.worth / self.tax
        return res_tax


class CountryHouse(Property):


    # , предлагаю сумму налога tax переопределять в методе init =)

    def __init__(self, worth):
        super().__init__(worth)
        self.tax = 500

    def tax_calculation(self):
        res_tax = self.worth / self.tax
        return res_tax


print("Для рассчета налога - введите количество денег и стоимость имущества: ")
bank = int(input("Количество денег: "))
car_price = int(input("Стоимость машины: "))
appartament_price = int(input("Стоимость аппартаментов: "))
house_price = int(input("Стоимость дачи: "))
car = Car(car_price)
appartament = Appartment(appartament_price)
house = CountryHouse(house_price)

if bank >= car.tax_calculation() + appartament.tax_calculation() + house.tax_calculation():
    print(
        "Для оплаты транспортного налога {}, налога на аппартменты {}, налога на дачу {} у Вас достаточно средств".format(
            car.tax_calculation(), appartament.tax_calculation(), house.tax_calculation()
        ))
else:
    credit = bank - car.tax_calculation() - appartament.tax_calculation() - house.tax_calculation()
    print(
        "Для оплаты транспортного налога {}, налога на аппартменты {}, налога на дачу {} у Вас недостаточно средств".format(
            car.tax_calculation(), appartament.tax_calculation(), house.tax_calculation()
        ))
    print("Что бы оплатить нужно еще денег: {}".format(abs(credit)))
