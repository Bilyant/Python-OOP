def reverse_text(string: str):
    num = 1
    while num <= len(string):
        yield string[-num]
        num += 1


for char in reverse_text("step"):
    print(char, end='')
