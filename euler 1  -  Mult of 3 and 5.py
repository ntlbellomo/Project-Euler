# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def ar(x):
    return x*(x+1)


n = 1000
n -= 1
a = int(n/3)
b = int(n/5)
c = int(n/15)

# Using the Sum of Arithmetic Progression Sn = (n/2) * {2*a + (n-1)*d}
# Where, n -> total number of terms a -> first term d -> common difference
# Sn_3=3*ar(a)/2 ; Sn_5=5*ar(a)/2 ; Sn_15=15*ar(a)/2

print(int(int(3*ar(a) + 5*ar(b) - 15*ar(c)) >> 1))
