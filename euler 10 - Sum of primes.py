# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math

teto = 2*(10**6)+1
lista = []
total = [True] * teto

# Like problem 7, we use the sieve of eratostenes

for i in range(2, int(round(math.sqrt(teto)))):
    for j in range(i*i, teto, i):
        total[j] = False
for w in range(2, teto):
    if total[w] == True:
        lista.append(w)

somatorio = sum(lista)

print(somatorio)
