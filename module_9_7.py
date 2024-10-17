def is_prime(func):
    def wrapper(*args):
        sum = func(*args)
        if sum % 2 == 0:
            print('Simple')
        else:
            print('Composite')
        return sum
    return wrapper

@is_prime
def sum_three(*list_):
    result = 0
    for i in list_:
        result += i
    return result

sum = sum_three(2, 3, 6)
print(sum)