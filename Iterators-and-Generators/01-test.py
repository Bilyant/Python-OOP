class CustomRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            current = self.start
            self.start += 1
            return current
        else:
            raise StopIteration()


one_to_ten = CustomRange(1, 10)
for num in one_to_ten:
    print(num)
