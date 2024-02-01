def squares(n):
    num = 1
    while num <= n:
        yield num ** 2
        num += 1


print(list(squares(5)))
# [1, 4, 9, 16, 25]
