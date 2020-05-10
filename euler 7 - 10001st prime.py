# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

import math

# Brute force, calculate every prime ultil 10001

limite = 10002
numero = 2
p = 1
primo = 1
i = 2

while p < limite:
    i = int(round(math.sqrt(numero)))
    while i > 1:
        if numero % i == 0:
            break
        i -= 1
    else:
        if numero > primo:
            primo = numero
        p += 1
    numero += 1

print(primo)

# If we have a rough ideia of the order of magnitude of the prime
# we can use the sieve of eratostenes (crivo de eratostenes)
# Algo a lot faster

limite_siev = 10001
prim = {i for i in range(2, 105000)}
for i in range(2, 325):
    prim = prim.difference({i for i in range(i*2, 400000, i)})
prim = list(sorted(prim))

print(prim[limite_siev-1])
