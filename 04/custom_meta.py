class CustomMeta(type):
    def __new__(mcs, name, bases, class_dict, **kwargs):
        custom_class_dict = {'__setattr__': mcs.__setattr__}

        for key, value in class_dict.items():
            if key.startswith('__') and key.endswith('__'):
                key_custom_class_dict = key
            else:
                key_custom_class_dict = f'custom_{key}'
            custom_class_dict[key_custom_class_dict] = value

        return super().__new__(mcs, name, bases, custom_class_dict)

    def __setattr__(cls, name, val):
        if name.startswith('__') and name.endswith('__'):
            key = name
        else:
            key = f'custom_{name}'
        cls.__dict__[key] = val


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
