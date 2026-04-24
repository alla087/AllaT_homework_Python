from address import Address
from mailing import Mailing

# Создаем адреса
from_address = Address("123456", "Москва", "Тверская", "1", "101")
to_address = Address("654321", "Санкт-Петербург", "Невский", "10", "15")

# Создаем почтовое отправление
mailing = Mailing(to_address, from_address, 150, "TRACK12345")

# Вывод информации об отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")