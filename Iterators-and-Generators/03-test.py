class vowels:
    def __init__(self, string: str):
        self.string = string
        self.start = 0
        self.end = len(string)
        self.vowels = []
        self.searched_chars = ('a', 'e', 'i', 'o', 'u', 'y')

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <  self.end:
            current = self.string[self.start]
            self.start += 1
            if current.lower() in self.searched_chars:
                return current
        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
