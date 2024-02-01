from collections import deque


def fibonacci():
    first_n, second_n = 0, 1
    while True:
        yield first_n
        first_n, second_n = second_n, first_n + second_n


generator = fibonacci()
for i in range(5):
    print(next(generator))
