# перенёс код. Пожалуйста обратите внимание, сначала пишем функции, потом остальной код =)
def chek_key(val):
    for key, value in country_dict.items():
        if val == value:
            return key


countries = int(input("Количество стран: "))
country_dict = dict()

for i_country in range(1, countries + 1):
    print("{} страна: ".format(i_country), end=" ")
    # TODO, предлагаю попробовать объединить переменные country и country_list в одну.
    country = input()
    country_list = country.split()
    # TODO, для сокращения количества [][] в коде, предлагаю создать переменную
    #  для country_list[0] и далее в коде работать с ней.
    country_dict[country_list[0]] = []
    for i_city in country_list[1:]:
        country_dict[country_list[0]].append(i_city)
print(country_dict)

for i_city in range(1, 4):
    print("{} город:".format(i_city))
    city = input()
    for i_city in country_dict.values():
        if city in i_city:
            print("Город {} расположен в стране".format(city), chek_key(i_city))
            break
    else:
        print("По городу {} нет данных".format(city))
