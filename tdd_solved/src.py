def my_function(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise Exception()
    if b == 0:
        return 0
    return round(a / b)
