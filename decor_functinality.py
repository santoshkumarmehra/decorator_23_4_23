def outer(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner

@outer
def print_str():
    return "hello sam"
print(print_str())
