def vowel_filter(function):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    def wrapper():
        to_be_filtered = function()
        result = [ch for ch in to_be_filtered if ch.lower() in vowels]
        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
