"""
Check if a number is prime or not.
"""

#Using flag variable
n = int(input("Enter a number:"))
print(int(n ** 0.5))
if n <= 1:
    print(False)
else:
    prime = True

    for i in range(2, int(n**0.5)+1):   # (n**0.5) it means (√n)
        if n % i == 0:
            prime = False
            break
    print(prime)



#----------------------------------------------------------------------------

#Using isprime() method
"""
If you don't have sympy on your machine, install it with pip:
    $ pip install sympy
"""
from sympy import isprime


n = int(input("Enter the number: "))
prime = isprime(n)
print(prime)

#----------------------------------------------------------------------------
#Using Sieve of Eratosthenes
"""
This method creates a list of numbers and marks multiples 
of each number as non-prime until the target number is reached.
"""

def is_prime(n):
    if n < 2:
        return False

    s = [True] * (n + 1) #It creates a Boolean list from index 0 to n.
    s[0] = s[1] = False #Treating 0 and 1 as False
    print(s)

    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:    #If it is still marked as prime, then eliminate its multiples.
            for j in range(i * i, n + 1, i): #Setting Multiples to False
                s[j] = False
    print(s)
    return s[n]
n = int(input("Enter a number: "))

print(is_prime(n))


#----------------------------------------------------------------------------
#Using Recursion

from math import sqrt


def prime(n, i):
    if i == 1:
        return True
    if n % i == 0:
        return False
    return prime(n, i - 1)

n = int(input("Enter a number: "))

print(prime(n, int(sqrt(n))))



#----------------------------------------------------------------------------

def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # Exclude all other even numbers
    if n % 2 == 0:
        return False

    # Check odd factors up to the square root of n
    # int(n**0.5) + 1 calculates the integer square root limit
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False  # Found a factor, so it's not prime

    return True  # No factors found, it is prime


# Example Usage:
print(is_prime(11))  # Returns: True
print(is_prime(4))  # Returns: False