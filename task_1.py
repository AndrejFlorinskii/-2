import doctest


class Storage:
    def __init__(self, Storage_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Хранилище"

        :param Storage_volume: Объем памяти хранилища
        :param occupied_volume: Объем занимаемой памяти хранилища

        Примеры:
        >>> storage = Storage(128, 61)  # инициализация экземпляра класса
        """
        if not isinstance(Storage_volume, (int, float)):
            raise TypeError("Объём памяти хранилища должен быть типа int или float")
        if Storage_volume > 128:
            raise ValueError("Объем памяти хранилища не должен быть больше 128 Гбайт")
        self.Storage_volume = Storage_volume


        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объем занимаемой памяти хранилища должен быть int или float")
        if occupied_volume > Storage_volume:
            raise ValueError("Объем занимаемой памяти хранилища не может быть больше памяти хранилища")
        self.occupied_volume = occupied_volume

    def is_overloaded_storage(self) -> bool:
        """
        Функция, которая проверяет, заполнена ли память более, чем на 90%

        :return: Перегружена ли память

        Примеры:
        >>> storage = Storage(128, 125)
        >>> storage.is_overloaded_storage()
        """
        ...

    def add_files_to_storage(self, file: float) -> None:
        """
        Добавление файлов в память.
        :param file: Размер загружаемого файла.

        :raise ValueError: Если размер загружаемого файла превышает свободное место в памяти, то вызываем ошибку

        Примеры:
        >>> storage = Storage(128, 43)
        >>> storage.add_files_to_storage(2)
        """
        if not isinstance(file, (int, float)):
            raise TypeError("Загружаемый файл должен быть типа int или float")
        if file > self.Storage_volume - self.occupied_volume:
            raise ValueError("Загружаемый файл должен быть меньше объема свободной памяти")
        ...

    def remove_file_from_storage(self, estimate_file: float) -> None:
        """
        Удаление файлов из памяти.

        :param estimate_file: Размер удаляемого файла
        :raise ValueError: Если размер удаляемого файла превышает объем занимаемой памяти хранилища,
        то возвращается ошибка.

        :return: Размер реально удаляемого файла

        Примеры:
        >>> storage = Storage(128, 50)
        >>> storage.remove_file_from_storage(10)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # Тестирование примеров, которые находятся в документации





import doctest


class Powerline:
    def __init__(self, Voltage_class: float, Voltage: float):
        """
        Создание и подготовка к работе объекта "ЛЭП"

        :param Voltage_class: Класс напряжения ЛЭП
        :param Voltage: Фактическое напряжение ЛЭП

        Примеры:
        >>> powerline = Powerline(220, 230)  # инициализация экземпляра класса
        """
        if not isinstance(Voltage_class, (int, float)):
            raise TypeError("Класс напряжения ЛЭП должен быть типа int или float")
        if Voltage_class not in (6, 10, 20, 35, 110, 150, 220, 330, 500, 750, 1150):
            raise ValueError("Класс напряжения ЛЭП должен соответствовать эксплуатируемым в России классам")
        self.Voltage_class = Voltage_class


        if not isinstance(Voltage, (int, float)):
            raise TypeError("Фактическое напряжение ЛЭП должно быть int или float")
        if Voltage > 1.2 * Voltage_class:
            raise ValueError("Фактическое напряжение ЛЭП не должно превышать наибольшее рабочее напряжение - величину класса напряжения более, чем на 20%")
        self.Voltage = Voltage

    def is_decrease_voltage(self) -> bool:
        """
        Функция, которая проверяет, снижается ли напряжение более, чем на 10%

        :return: Пониженное ли напряжение

        Примеры:
        >>> powerline = Powerline(330, 300)
        >>> powerline.is_decrease_voltage()
        """
        ...

    def increase_voltage_transformer(self, tap: float) -> None:
        """
        Увеличение напряжения на высокой стороне повышающего трансформатора.
        :param tap: Величина напряжения отпайки.

        :raise ValueError: Если величина напряжения отпайки в сумме с фактическим напряжением превышает наибольшее рабочее напряжение, то вызываем ошибку.

        Примеры:
        >>> powerline = Powerline(330, 340)
        >>> powerline.increase_voltage_transformer(3)
        """
        if not isinstance(tap, (int, float)):
            raise TypeError("Величина напряжения отпайки должна быть типа int или float")
        if tap + self.Voltage > self.Voltage_class * 1.2:
            raise ValueError("Величина напряжения отпайки не должна быть больше наибольшего рабочего напряжения")
        ...



if __name__ == "__main__":
    doctest.testmod()  # Тестирование примеров, которые находятся в документации




import doctest


class Painting:
    def __init__(self, artist_surname: str, year: float):
        """
        Создание и подготовка к работе объекта "Картина"

        :param artist_surname: Фамилия художника
        :param year: Год создания

        Примеры:
        >>> painting = Painting("Крамской", 1876)  # инициализация экземпляра класса
        """
        if not isinstance(artist_surname, (str)):
            raise TypeError("Фамилия художника должна быть типа int")
        if artist_surname not in (
                "Крамской",
                "Шишкин",
                "Васнецов",
                "Серов",
                "Рублёв",
                "Айвазовский",
                "Репин",
                "Иванов",
                "Суриков",
                "Кандинский"
                ):
            raise ValueError("Фамииля художника только из тех, чьи картины представлены на временной экспозиции")
        self.artist_surname = artist_surname


        if not isinstance(year, (int, float)):
            raise TypeError("Год создания картины должен быть int или float")
        if year > 2024:
            raise ValueError("Год создания картины ограничен 2024 годом")
        self.year = year

    def is_special_draw_school(self) -> bool:
        """
        Функция, которая проверяет, относится ли художник к школе передвижников

        :return: Передвижник или нет

        Примеры:
        >>> painting = Painting("Шишкин", 1860)
        >>> painting.is_special_draw_school()
        """
        ...

    def is_artist_19_century(self) -> bool:
        """
        Относится ли картина к искусству 19 века.
        :return: 19 век иил нет

        :raise ValueError: Если год создания картины не относится к 19 веку, то вызываем ошибку.

        Примеры:
        >>> painting = Painting("Иванов", 1860)
        >>> painting.is_artist_19_century()
        """

        if not 1799 < self.year < 1900:
            raise ValueError("Год написания картины не относится к 19 веку")
        ...



if __name__ == "__main__":
    doctest.testmod()  # Тестирование примеров, которые находятся в документации