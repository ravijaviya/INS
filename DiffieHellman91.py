from math import fmod


def primes_sieve(limit):
    a = [True] * limit  # Initialize the primarily list
    a[0] = a[1] = False

    for (i, isPrime) in enumerate(a):
        if isPrime:
            yield i
            for n in range(i * i, limit, i):  # Mark factors non-prime
                a[n] = False
    return a


def binaryMod(x, e, y):
    temp = 1  # d as temp
    binary = bin(e)[2:]
    for i in binary:
        if i == '0':
            temp = fmod(temp * temp, y)
        elif i == '1':
            temp = fmod(temp * temp, y)
            temp = fmod(temp * x, y)
    return int(temp)


def primitiveRoot(x, y):
    l = set()
    for i in range(1, x):
        temp = binaryMod(y, i, x)
        l.add(temp)
    if len(l) == x - 1:
        return True
    else:
        return False


q = int(input("Enter q:"))
prime = primes_sieve(q + 1)
if q in prime:
    alpha = int(input("Enter Alpha:"))
    if primitiveRoot(q, alpha):
        Xa = int(input("Enter private key of A:"))
        Xb = int(input("Enter private key of B:"))
        Ya = binaryMod(alpha, Xa, q)
        Yb = binaryMod(alpha, Xb, q)
        Ka = binaryMod(Ya, Xb, q)
        Kb = binaryMod(Yb, Xa, q)
        if Ka == Kb:
            key = Ka
            print("Key is :", key)
        else:
            print("key does not match...")
    else:
        print("Enter valid primitive root of q...")
else:
    print("Enter prime number...")
