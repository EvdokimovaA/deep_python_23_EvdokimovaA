import io
import pstats
import weakref
import cProfile
import time
from memory_profiler import profile


class DefaultClass:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


class SlotsClass:
    __slots__ = ("attr1", "attr2")

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


class WeakClass:
    def __init__(self, attr1, attr2):
        self.attr1 = weakref.ref(attr1)
        self.attr2 = weakref.ref(attr2)


class ForProfileClass1:
    pass


class ForProfileClass2:
    pass


@profile
def create_default(n):
    defaults = [DefaultClass(ForProfileClass1(), ForProfileClass2()) for _ in range(n)]
    return defaults


@profile
def create_slots(n):
    slots = [SlotsClass(ForProfileClass1(), ForProfileClass2()) for _ in range(n)]
    return slots


@profile
def create_weak(n):
    weaks = [WeakClass(ForProfileClass1(), ForProfileClass2()) for _ in range(n)]
    return weaks


@profile
def change_default(defaults):
    for element in defaults:
        element.attr1 = ForProfileClass2()
        element.attr2 = ForProfileClass1()


@profile
def change_slots(slots):
    for element in slots:
        element.attr1 = ForProfileClass2()
        element.attr2 = ForProfileClass1()


@profile
def change_weak(weaks):
    for element in weaks:
        element.attr1 = ForProfileClass2()
        element.attr2 = ForProfileClass1()


if __name__ == "__main__":
    N = 100000
    profile = cProfile.Profile()
    profile.enable()

    start_time = time.time()
    list_defaults = create_default(N)
    end_time = time.time()
    print(f'Время создания экземпляров DefaultClass: {end_time - start_time}')

    start_time = time.time()
    list_slots = create_slots(N)
    end_time = time.time()
    print(f'Время создания экземпляров SlotsClass: {end_time - start_time}')

    start_time = time.time()
    list_weaks = create_weak(N)
    end_time = time.time()
    print(f'Время создания экземпляров WeakClass: {end_time - start_time}')

    start_time = time.time()
    change_default(list_defaults)
    end_time = time.time()
    print(f'Время изменения экземпляров DefaultClass: {end_time - start_time}')

    start_time = time.time()
    change_slots(list_slots)
    end_time = time.time()
    print(f'Время изменения экземпляров SlotsClass: {end_time - start_time}')

    start_time = time.time()
    change_weak(list_weaks)
    end_time = time.time()
    print(f'Время изменения экземпляров WeakClass: {end_time - start_time}')

    profile.disable()
    info = io.StringIO()
    sort_by = "cumulative"
    stats = pstats.Stats(profile, stream=info).sort_stats(sort_by)
    stats.print_stats()
    print(info.getvalue())
