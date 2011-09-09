def memo(func):
    values = {}
    def memoized_func(*args):
        if args in values:
            return values[args]
        else:
            values[args] = func(*args)
            return values[args]
    memoized_func.values = values
    return memoized_func
