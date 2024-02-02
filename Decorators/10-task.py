def tags(html_tag):
    def decorator(func):
        def wrapper(*args):
            txt = func(*args)
            return f'<{html_tag}>{txt}</{html_tag}>'

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))

print()

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
