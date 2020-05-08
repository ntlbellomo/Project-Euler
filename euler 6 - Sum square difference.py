# The sum of the squares of the first ten natural numbers is,
# 1^2+2^2+...+10^2=385
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)^2=55^2=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

numero = 100
soma_quadrados = 0
somatorio = 0

# Calculate the two sums and calculate the difference

for i in range((numero+1)):
    soma_quadrados += i*i

for j in range((numero+1)):
    somatorio += j

quadrado_somatorio = somatorio * somatorio
diff = soma_quadrados - quadrado_somatorio

print(diff*(-1))
