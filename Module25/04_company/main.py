class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age


class Employee(Person):

    def payroll_calculation(self):
        self.salary = 13000


class Manager(Employee):

    # TODO, предлагаю определить этот метод в классе Employee.
    #  В таком случае, в остальных классах его определять будет не нужно. =)
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.name = name
        self.surname = surname

    def payroll_calculation(self):
        salary = 13000
        return salary

    def info(self):
        print("{} {} заработал в этом месяце {}".format(self.name, self.surname, self.payroll_calculation()))


class Agent(Employee):
    volume_sale = 100000

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.name = name
        self.surname = surname

    def payroll_calculation(self):
        salary = 5000 + (self.volume_sale * 0.05)
        return salary

    def info(self):
        print("{} {} заработал в этом месяце {}".format(self.name, self.surname, self.payroll_calculation()))


class Worker(Employee):
    hours_worked = 55

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.name = name
        self.surname = surname

    def payroll_calculation(self):
        salary = 100 * self.hours_worked
        return salary

    def info(self):
        print("{} {} заработал в этом месяце {}".format(self.name, self.surname, self.payroll_calculation()))


manager1 = Manager("Tom", "Abramson", 25)
manager1.info()
manager2 = Manager("Tim", "Anderson", 25)
manager2.info()
manager3 = Manager("David", "Attwood", 25)
manager3.info()
agent1 = Agent("Jacob", "Clapton", 25)
agent1.volume_sale = 80000
agent1.info()
agent2 = Agent("James", "Davidson", 25)
agent2.volume_sale = 95000
agent2.info()
agent3 = Agent("Riley", "Cramer", 25)
agent3.volume_sale = 75000
agent3.info()
worker1 = Worker("Charlie", "Dickinson", 25)
worker1.hours_worked = 25
worker1.info()
worker2 = Worker("Alfie", "Cook", 25)
worker2.hours_worked = 48
worker2.info()
worker3 = Worker("Jack", "Derrick", 25)
worker3.hours_worked = 72
worker3.info()
