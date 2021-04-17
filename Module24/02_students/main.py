import random
import operator


class Student:

    def __init__(self, name):
        self.name = name
        self.group_number = random.randint(100, 115)
        self.educational_performance = [random.randint(2, 5) for _ in range(5)]
        self.average_rating = self.sort_performance()

    def info(self):
        print("Имя: {}, номер группы: {}, успеваемость {}".format(
            self.name, self.group_number, self.educational_performance))

    def sort_performance(self):
        result = 0
        for item in self.educational_performance:
            result += item
        return result


students = list()
for name in range(1, 11):
    students.append(Student("student_{}".format(name)))

students.sort(key=operator.attrgetter("average_rating"))

for item in students:
    item.info()

# зачёт!
