 # Prime Number Sieve
 # http://inventwithpython.com/hacking (BSD Licensed)
import math
def isPrime(num):
    if num < 2:
         return False
    for i in range(2, int(math.sqrt(num)) + 1):
         if num % i == 0:
            return False
    return True
    print(num)
def primeSieve(sieveSize):
     sieve = [True] * sieveSize
     sieve[0] = False
     sieve[1] = False
     for i in range(2, int(math.sqrt(sieveSize)) + 1):
         pointer = i * 2
         while pointer < sieveSize:
             sieve[pointer] = False
             pointer += i
     primes = []
     for i in range(sieveSize):
         if sieve[i] == True:
             primes.append(i)

     return primes