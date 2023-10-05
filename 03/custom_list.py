class CustomList(list):
    @staticmethod
    def _check_correct_type(other):
        if not isinstance(other, (list, CustomList)):
            raise TypeError("Ожидался тип данных list или CustomList")

    @staticmethod
    def do_equal_len(lst1, lst2):
        new_lst1, new_lst2 = lst1.copy(), lst2.copy()
        length_difference = len(lst1) - len(lst2)
        if length_difference > 0:
            new_lst2 += [0] * length_difference
        elif length_difference < 0:
            new_lst1 += [0] * -length_difference
        return new_lst1, new_lst2

    def __add__(self, other):
        CustomList._check_correct_type(other)
        lst, other_lst = self.do_equal_len(self, other)
        result = [lst[i] + other_lst[i] for i in range(len(lst))]
        return CustomList(result)

    def __radd__(self, other):
        CustomList._check_correct_type(other)
        return self.__add__(other)

    def __sub__(self, other):
        CustomList._check_correct_type(other)
        lst, other_lst = self.do_equal_len(self, other)
        result = [lst[i] - other_lst[i] for i in range(len(lst))]
        return CustomList(result)

    def __rsub__(self, other):
        CustomList._check_correct_type(other)
        lst, other_lst = self.do_equal_len(self, other)
        result = [other_lst[i] - lst[i] for i in range(len(lst))]
        return CustomList(result)

    def __lt__(self, other):
        CustomList._check_correct_type(other)
        return sum(self) < sum(other)

    def __le__(self, other):
        CustomList._check_correct_type(other)
        return sum(self) <= sum(other)

    def __eq__(self, other):
        CustomList._check_correct_type(other)
        return sum(self) == sum(other)

    def __ne__(self, other):
        CustomList._check_correct_type(other)
        return sum(self) != sum(other)

    def __gt__(self, other):
        CustomList._check_correct_type(other)
        return sum(self) > sum(other)

    def __ge__(self, other):
        CustomList._check_correct_type(other)
        return sum(self) >= sum(other)

    def __str__(self):
        lst_str = super().__str__()
        return f'{lst_str} Сумма: {sum(self)}'
