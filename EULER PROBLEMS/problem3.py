from sympy import factorint

def largest_prime_factor(n):
    factors = factorint(n)
    return max(factors.keys())

number = 600851475143
print(largest_prime_factor(number))