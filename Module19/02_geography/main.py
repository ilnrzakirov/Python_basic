
countries = int(input("Количество стран: "))
country_dict = dict()

for i_country in range (1, countries + 1):
    print("{} страна: ".format(i_country), end=" ")
    country = input()
    country_list = country.split()
    country_dict[country_list[0]] = []
    for i_city in country_list [1:]:
        country_dict[country_list[0]].append(i_city)
print(country_dict)

def chek_key (val):
    for key, value in country_dict.items():
        if val == value:
            return key

for i_city in range (1,4):
    print("{} город:".format(i_city))
    city = input()
    for i_city in country_dict.values():
        if city in i_city:
            print("Город {} расположен в стране".format(city), chek_key(i_city))
            break
    else:
        print("По городу {} нет данных".format(city))

