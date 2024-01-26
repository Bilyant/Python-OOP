start_count = int(input('Number: '))


def stars_rhombus(size):
    result = []
    for i in range(1, size + 1):  # upper part
        spaces = ' ' * (size - i)
        stars = '*' * i
        result.append(spaces + ' '.join(stars))
    for i in range(size-1, 0, -1):  # bottom part
        spaces = ' ' * (size - i)
        stars = '*' * i
        result.append(spaces + ' '.join(stars))

    return '\n'.join(result)


print(stars_rhombus(start_count))
print(dir())
print(vars())
