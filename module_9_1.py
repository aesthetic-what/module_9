def apply_all_func(list_, *functions):
    all_func = {}

    for func in functions:
        all_func[func.__name__] = func(list_)
    return all_func


def min_value(list_):
    return min(list_)


def max_value(list_):
    return max(list_)


def len_value(list_):
    return len(list_)


def sum_value(list_):
    return sum(list_)


def sorted_value(list_):
    return sorted(list_)


print(apply_all_func([6, 20, 15, 9], min, max))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

