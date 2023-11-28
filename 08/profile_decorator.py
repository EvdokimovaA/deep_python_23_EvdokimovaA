import cProfile
import pstats
import io


def profile_decorator(func):
    profiles_dict = {}

    def wrapper(*args, **kwargs):

        if func.__name__ not in profiles_dict:
            profiles_dict[func.__name__] = cProfile.Profile()

        profile = profiles_dict[func.__name__]
        profile.enable()
        result = func(*args, **kwargs)
        profile.disable()

        return result

    def print_stat():
        for func_name, profile in profiles_dict.items():
            print(f"Stats for {func_name}:")
            string = io.StringIO()
            pstat = pstats.Stats(profile, stream=string)
            pstat.print_stats()
            print(string.getvalue())

    wrapper.print_stat = print_stat
    return wrapper


@profile_decorator
def add(value_a, value_b):
    return value_a + value_b


@profile_decorator
def sub(value_a, value_b):
    return value_a - value_b


if __name__ == "__main__":
    add(1, 2)
    add(4, 5)
    add(5, 5)
    sub(4, 5)

    add.print_stat()
    sub.print_stat()
