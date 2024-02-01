def genrange(start: int, end: int):
    num = start
    while num <= end:
        yield num
        num += 1


print(list(genrange(1, 10)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
