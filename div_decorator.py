def division_decorator(func):
    def inner(x, y):
        if y==0:
            return "give proper output"
        return func(x, y)
    return inner

@division_decorator
def div_value(a, b):
    return a/b
print(div_value(10, 20))