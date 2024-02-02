def logged(func):
    def wrapper(*args):
        return f'you called {func.__name__} it returned {func(*args)}'

    return wrapper


@logged
def add_three_to_len(*args):
    return 3 + len(args)


print(add_three_to_len(4, 4, 4))
