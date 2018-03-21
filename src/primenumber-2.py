from math import sqrt
import json

def is_prime(x):
    prime = False
    if x > 1:
        prime = True
        k = 2
        n = sqrt(x) # to find square of x only once (or n = x ** 0.5 to get rid of math module)
        while k <= n and prime == True:
            if x % k == 0:
                prime = False
            k += 1
    return prime
f = open('/Users/vskdtc/Documents/primenumber-2.json', 'w')
num = 1 # try num = 1011013, num = 10110133, num = 101101331
for num in range(1000000):
    if is_prime(num):
        num =[str(num), " is a prime number"]
        json.dump(num, f, sort_keys=True)
        f.write('\n')
       # print str(num) + " is a prime number"
    else:
        num =[str(num), " is a composite number"]
        #json.dump(num, f, sort_keys=True)
        #f.write('\n')
        #print str(num) + " is a composite number"