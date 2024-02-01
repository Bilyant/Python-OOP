class CountdownIterator:
    def __init__(self, count: int):
        self.count = count
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.count:
            current = self.count - self.num
            self.num += 1
            return current
        raise StopIteration


iterator = CountdownIterator(10)
for item in iterator:
    print(item, end=" ")

print()

iterator = CountdownIterator(0)
for item in iterator:
    print(item, end=" ")
