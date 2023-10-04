import time


def mean(k):
    def decorator(func):
        last_executions = []

        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()

            last_executions.append(end_time - start_time)

            if not isinstance(k, int):
                raise TypeError("Ожидалось целое число")
            if k <= 0:
                raise ValueError("Ожидалось положительное целое число")

            if len(last_executions) < k:
                average_execution_time = sum(last_executions) / len(last_executions)
            else:
                average_execution_time = sum(last_executions[-k:]) / k
            print(average_execution_time)
            return average_execution_time

        return wrapper

    return decorator
