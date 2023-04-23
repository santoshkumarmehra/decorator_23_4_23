def outer():
    x=10
    def innner():
        y=20
        result = x+y
        return result
    return innner()
a = outer()
print(a)



