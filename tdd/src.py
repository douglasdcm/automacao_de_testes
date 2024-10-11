def my_function(a, b):
    if b == 0:
        return 0
    if not isinstance(a, int) or not isinstance(b, int):
        raise Exception()
    return round(a / b)
