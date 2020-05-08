# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

maior = 0
a = 0
b = 0
# Algo will multiply every new pair (x,y) in (100,999)x(100,999)
# and check if the number reversed is a polindrome and save the biggest
# To reduce the algo execution time,
# I will use the fact that a palindrome with an even number of digits is divible by 11

for i in range(100+a, 999):
    for j in range(100+b, 999):
        number = i*j
        if number % 11 == 0:
            para_testar = str(number)
            contrario = para_testar[::-1]
            if para_testar == contrario:
                if number > maior:
                    maior = i*j
    a += 1
    b += 1

print(maior)
