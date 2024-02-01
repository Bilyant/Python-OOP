def solution():

    """generates an infinite amount of integers (starting from 1)"""
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    """generates the halves of those integers (each integer / 2)"""
    def halves():
        for i in integers():
            yield i / 2

    """takes the first n halves of those integers"""
    def take(n, seq):
        n_halves = []
        for i in range(n):
            n_halves.append(next(seq))
        return n_halves

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

print()

take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
