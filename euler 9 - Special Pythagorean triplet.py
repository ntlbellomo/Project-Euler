# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Lets use the relation given to reduce 1 Degree of freedom and the Triangle inequality
# a^2+b^2=c^2 c=1000-a-b


def triplet():

    for x in range(1000):
        for y in range(1000):
            if y > x:
                z = 1000-(x+y)
                if z > y:
                    if x+y > z and z > y-z and z+x > y and y > z-x and z+y > x and x > z-y:
                        if x*x + y*y == z*z:
                            a = x
                            b = y
                            c = z
                            d = a*b*c
                            return a, b, c, d


print(triplet())
