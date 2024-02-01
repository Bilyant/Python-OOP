class DictionaryIter:
    def __init__(self, dict_obj: {}):
        self.dict_obj = dict_obj
        self.data = list(dict_obj.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.dict_obj):
            current = tuple(self.data[self.idx])
            self.idx += 1
            return current
        raise StopIteration()


result = DictionaryIter({1: "1", 2: "2"})
for x in result:
    print(x)
"""
expected output:
    (1, '1')
    (2, '2')
"""
print()

result = DictionaryIter({"name": "Peter", "age": 24})
for x in result:
    print(x)
"""
expected output:
    ("name", "Peter")
    ("age", 24)
"""