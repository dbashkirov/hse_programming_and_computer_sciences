# **Задание**: написать декоратор `reverse_args` который изменяет порядок позиционных аргументов,
# переданных функции, на обратный

def reverse_args(f):

    def wrapper(*args, **kwargs):
        return f(*args[::-1], **kwargs)

    return wrapper


@reverse_args
def f(*args):
    return sum([(i + 1) * arg for i, arg in enumerate(args)])


def g(*args):
    return sum([(i + 1) * arg for i, arg in enumerate(args)])


print(f(1, 2, 3, 4, 5))
print(g(1, 2, 3, 4, 5))