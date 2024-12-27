class IncorrectVinNumber(Exception):                        # Определение класса исключения для неверных vin номеров
    def __init__(self, message):
        self.message = message                              # Хранение сообщения об ошибке

class IncorrectCarNumbers(Exception):                       # Определение класса исключения для неверных номеров
    def __init__(self, message):                            # автомобиля
        self.message = message                              # Хранение сообщения об ошибке

class Car:                                                  # Определение класса для автомобилей
    def __init__(self, model, vin, numbers):
        self.model = model                                  # Установка названия модели автомобиля
        self.__vin = self.__is_valid_vin(vin)               # Проверка vin номера при инициализации
        self.__numbers = self.__is_valid_numbers(numbers)   # Проверка номера автомобиля при инициализации

    def __is_valid_vin(self, vin_number):                   # Проверка корректности vin номера
        if not isinstance(vin_number, int):                 # Проверка, является ли vin_number целым числом
            raise IncorrectVinNumber('Некорректный тип vin номер')  # Выбрасываем исключение, если тип некорректен

        if vin_number < 1000000 or vin_number > 9999999:    # Проверка, находится ли vin_number в допустимом диапазоне
            raise IncorrectVinNumber('Неверный диапазон для vin номера')  # Выбрасываем исключение для некорректного диапазона
        return vin_number                                   # Возвращаем правильное значение vin номера

    def __is_valid_numbers(self, numbers):                  # Проверка корректности номеров автомобиля
        if not isinstance(numbers, str):                    # Проверка, является ли numbers строкой
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')  # Выбрасываем исключение, если тип некорректен

        if len(numbers) != 6:                               # Проверка, имеет ли строка длину ровно 6 символов
            raise IncorrectCarNumbers('Неверная длина номера')  # Выбрасываем исключение для некорректной длины
        return numbers                                      # Возвращаем верное значение номера автомобиля
# Пример выполнения кода:
try:
    first = Car('Model1', 1000000, 'f123dj') # Создание первого объекта Car с корректными параметрами
except IncorrectVinNumber as exc:
    print(exc.message)                          # Выводим сообщение об ошибке, если возникло исключение IncorrectVinNumber
except IncorrectCarNumbers as exc:
    print(exc.message)                          # Выводим сообщение об ошибке, если возникло исключение IncorrectCarNumbers
else:
    print(f'{first.model} успешно создан')      # Успешное создание объекта

try:
    second = Car('Model2', 300, 'т001тр')    # Создание второго объекта Car с некорректным vin номером
except IncorrectVinNumber as exc:
    print(exc.message)                                          # Выводим сообщение об ошибке
except IncorrectCarNumbers as exc:
    print(exc.message)                                          # Выводим сообщение об ошибке
else:
    print(f'{second.model} успешно создан')                     # Успешное создание объекта

try:
    third = Car('Model3', 2020202, 'нет номера')# Создание третьего объекта Car с некорректным номером
except IncorrectVinNumber as exc:
    print(exc.message)                                          # Выводим сообщение об ошибке
except IncorrectCarNumbers as exc:
    print(exc.message)                                          # Выводим сообщение об ошибке
else:
    print(f'{third.model} успешно создан')                      # Успешное создание объекта