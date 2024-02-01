class TakeSkip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.num = 0
        self.loops = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.loops < self.count:
            current = self.num
            self.num += self.step
            self.loops += 1
            return current
        else:
            raise StopIteration


numbers = TakeSkip(2, 6)
for number in numbers:
    print(number)

print()

numbers = TakeSkip(10, 5)
for number in numbers:
    print(number)
