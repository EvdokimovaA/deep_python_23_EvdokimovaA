import cProfile
import pstats
import io


def profile_decorator(func):
    class Wrapper:

        def __init__(self, func):
            self.func = func
            self.content = []

        def __call__(self, *args, **kwargs):
            profile = cProfile.Profile()
            profile.enable()
            self.func(*args, **kwargs)
            profile.disable()
            string = io.StringIO()
            pstat = pstats.Stats(profile, stream=string)
            pstat.print_stats()
            self.content.append(string.getvalue())

        def print_stat(self):
            print("\n".join(self.content))

    return Wrapper(func)


@profile_decorator
def add(value_a, value_b):
    return value_a + value_b


@profile_decorator
def sub(value_a, value_b):
    return value_a - value_b


if __name__ == "__main__":
    add(1, 2)
    add(4, 5)
    sub(4, 5)

    add.print_stat()
    sub.print_stat()
