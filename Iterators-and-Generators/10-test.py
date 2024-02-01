class SequenceRepeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.chars_count = 0
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.chars_count < self.number:
            if self.idx == len(self.sequence):
                self.idx = 0
            current = self.sequence[self.idx]
            self.idx += 1
            self.chars_count += 1
            return current
        raise StopIteration


result = SequenceRepeat('abc', 5)
for item in result:
    print(item, end='')

"""
abcab
"""

print()

result = SequenceRepeat('I Love Python', 3)
for item in result:
    print(item, end='')

"""
I L
"""
