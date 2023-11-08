# **Задание**: написать декоратор `retry_n_times`, который будет на вход принимать переменную `n` -
# количество вызовов функции

def retry_n_times(n):
    def decorator(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                f(*args, **kwargs)
        return wrapper
    return decorator


@retry_n_times(10)
def f():
    print("I'm working")


f()
