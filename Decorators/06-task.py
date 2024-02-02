def even_parameters(func_ref):
    message = 'Please use only even numbers!'

    def wrapper(*args):
        has_unallowed_data = [True for n in args if n.__class__.__name__ != 'int']
        if has_unallowed_data:
            return message

        has_odd_nums = [True for n in args if n % 2 == 1]
        if has_odd_nums:
            return message

        return func_ref(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))

print()


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
