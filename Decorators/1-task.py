def store_results(func):
    def wrapper(*args):
        with open('result.txt', 'a') as file:
            file.write(f'Function {func.__name__} was add called. Result: {func(*args)}\n')

    return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
