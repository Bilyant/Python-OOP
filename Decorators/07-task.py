def make_bold(func):
    def wrapper(*args):
        return f'<b>{func(", ".join(args))}</b>'

    return wrapper


def make_italic(func):
    def wrapper(*args):
        return f'<i>{func(", ".join(args))}</i>'

    return wrapper


def make_underline(func):
    def wrapper(*args):
        return f'<u>{func(", ".join(args))}</u>'

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))

print()


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
