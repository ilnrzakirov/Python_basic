import re

number = ['9999999999', '999999-999', '99999x9999']
i = 0

pettern = r'\b[89]\d{9}'

while i < len(number):
    if re.findall(pettern, number[i]):
        print(number[i], ': все в порядке')
    else:
        print(number[i], ": не подходит")
    i = i + 1