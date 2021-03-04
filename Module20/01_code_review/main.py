students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def interests (dict):
    all_interest = []
    total_len = 0
    for i_num in dict:
        student = dict[i_num]
        all_interest += (student['interests'])
        total_len += len(student['surname'])
    return all_interest, total_len

for id, i_age in students.items():
    age = i_age["age"]
    print(" ID = {}, возраст - {}".format(id, age))

print(interests(students))
