def is_prime(n):
    for u in range(2, n):
        if n % u == 0:
            return False
    return True


is_prime_0 = is_prime(12)
is_prime_1 = is_prime(13)
print("12", is_prime_0)
print("13", is_prime_1)
