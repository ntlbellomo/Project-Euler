# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

n = 600851475143
i = 1
max_div = 1

# Test if n is divisible by i ,
# simplify n by i until n is no longer divisible by i,
# add 1 to i ultil i is the largest prime factor

while i <= n:
    if n % i == 0:
        max_div = i
        n = n/i
    i += 1


print(max_div)
