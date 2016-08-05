import math


def primes_sieve(limit):
    a = [True] * limit  # Initialize the primarily list
    a[0] = a[1] = False

    for (i, isPrime) in enumerate(a):
        if isPrime:
            yield i
            for n in range(i * i, limit, i):  # Mark factors non-prime
                a[n] = False
    return a


p = int(input("Enter P:"))
q = int(input("Enter q:"))
prime = list(primes_sieve(max(p, q) + 1))
if p not in prime or q not in prime:
    print("Please Enter Prime Numbers Only...")
else:
    n = p * q
    r = (p - 1) * (q - 1)
    choice = int(input("\n\n1.Encryption\n2.Decryption\nEnter Your Choice:"))
    if choice == 1:
        e = int(input("Enter e:"))
        if e > r or math.gcd(r, e) != 1:
            print("Please enter valid e...")
        else:
            for i in range(0, ):
                temp = (r * i + 1) / e
                if temp - int(temp) == 0:
                    d = int(temp)
                    break
            plainText = int(input("Enter Plain Text:"))
            temp = 1  # d as temp
            binary = bin(e)[2:]
            for i in binary:
                if i == '0':
                    temp = math.fmod(temp * temp, n)
                elif i == '1':
                    temp = math.fmod(temp * temp, n)
                    temp = math.fmod(temp * plainText, n)
            cipherText = int(temp)
            print("Cipher Text:", cipherText)
    elif choice == 2:
        d = int(input("Enter d:"))
        if d > r or math.gcd(r, d) != 1:
            print("Please enter valid d...")
        else:
            for i in range(0, ):
                temp = (r * i + 1) / d
                if temp - int(temp) == 0:
                    e = int(temp)
                    break
            cipherText = int(input("Enter Cipher Text:"))
            temp = 1  # d as temp
            binary = bin(d)[2:]
            for i in binary:
                if i == '0':
                    temp = math.fmod(temp * temp, n)
                elif i == '1':
                    temp = math.fmod(temp * temp, n)
                    temp = math.fmod(temp * cipherText, n)
            plainText = int(temp)
            print("Plain Text:", plainText)
