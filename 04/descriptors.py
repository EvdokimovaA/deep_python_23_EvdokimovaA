class AgeDescriptor:
    def __init__(self):
        self.name = "age_descript"

    def __set__(self, instance, value):
        if instance is None:
            return None
        if not (isinstance(value, int) and 0 <= value < 125):
            raise ValueError('Недопустимое значение для возраста')
        return setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        if instance is None:
            return None
        return getattr(instance, self.name)


class DataDescriptor:
    def __init__(self):
        self.name = "data_descript"

    def __set__(self, instance, value):
        if instance is None:
            return None
        if not isinstance(value, str):
            raise ValueError('Недопустимое значение для строки')
        return setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        if instance is None:
            return None
        return getattr(instance, self.name)


class WeightDescriptor:
    def __init__(self):
        self.name = "weight_descript"

    def __set__(self, instance, value):
        if instance is None:
            return None
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError('Недопустимое значение для веса')
        return setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        if instance is None:
            return None
        return getattr(instance, self.name)


class Human:
    age = AgeDescriptor()
    name = DataDescriptor()
    weight = WeightDescriptor()

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
