# Написать декоратор, который будет кешировать результаты работы функции.
# На вход подается число n - размер кеша.

def cache(n):

    def cached_func(f):
        cache = {}
        def wrapper(*args, **kwargs):
            nonlocal cache
            if len(cache) >= n:
                del cache[args]
            if len(cache) < n:
                cache[args] = f(*args, **kwargs)
            if args in cache:
                return cache[args]
        return wrapper
    return cached_func



