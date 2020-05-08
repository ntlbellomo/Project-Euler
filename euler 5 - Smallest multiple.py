# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

mmc = 1

# For every number from 1 and 20, if mmc is not divisible by i,
# multiple mmc until mmc is divible by i

for i in range(1, 21):
    if not mmc % i == 0:
        for j in range(1, 21):
            if (mmc * j) % i == 0:
                mmc = mmc * j
                break

print(mmc)
