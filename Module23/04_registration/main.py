def chek(data):
    if len(data) != 3:
        return


registration_file = open("registrations.txt", "r")
for i_line in registration_file:
    person = i_line.split()
    result = chek(person)
