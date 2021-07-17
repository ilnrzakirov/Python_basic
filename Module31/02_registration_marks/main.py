import re

data = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

privat = re.findall(r'\b\D{1}\d{3}\D{2}\d{3}', data)
taxi = re.findall(r'\b\D{2}\d{3}\d{2,3}', data)

print("Список номеров частных автомобилей: ", privat)
print("Список номеров такси: ", taxi)