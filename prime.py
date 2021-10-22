n = 17
prime = True

for u in range(2, n):
    if n % u == 0:
        prime = False

print(prime)
