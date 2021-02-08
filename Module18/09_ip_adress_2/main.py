ip = input("Введите IP адресс: ").split(".")
for number in ip:
    if not number.isdigit():
        print(number, "не целое число")
        break
    elif int(number) > 255:
        print(number, "превышает 255")
        break
    elif len(ip) != 4:
        print("Адресс - это четыре числа, разделенные точками ")
        break
else:
    print("IP адресс корректен ")