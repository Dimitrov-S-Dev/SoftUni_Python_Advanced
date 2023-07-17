def is_prime(num):
    if num <= 1:
        return False
    for number in range(2, num):
        if num % number == 0:
            return False
    return True


def get_primes(ll):
    for num in ll:
        if is_prime(num):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))