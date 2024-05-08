import random
import math

p = int(input('Input a prime number as p: '))
q = int(input('Input a prime number as q: '))

def check_prime():
    global p
    global q
    if p <= 1:
        print(f'{p} is not a prime number')
        p = int(input(f'Input a prime number replace of {p}: '))
    if q <= 1:
        print(f'{q} is not a prime number')
        q = int(input(f'Input a prime number replace of {q}: '))
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            print(f'{p} is not a prime number')
            p2 = int(input(f'Input a prime number replace of {p}: '))
            p = p2
            check_prime()
    for i in range(2, int(q ** 0.5) + 1):
        if q % i == 0:
            print(f'{q} is not a prime number')
            q2 = int(input(f'Input a prime number replace of {q}: '))
            q = q2
            check_prime()

check_prime()

print(f'{p} and {q} is prime number')

n = p * q
phi_n = (p-1) * (q-1)

print(f'n = {n} and phi_n = {phi_n}')

e = random.randint(2, phi_n - 1)

def compute_e():
    global e
    while math.gcd(e, phi_n != 1):
        e = random.randint(2, phi_n - 1)
        print(f'public key is = {e}')
        return e

def modular_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

d = modular_inverse(e, phi_n)

print(f'private key is = {d}')
print(f'public key is = {e}')

plain_text = int(input('Input your integer message: '))

#encryption
C = pow(plain_text, e)
C = math.fmod(C, n)
print(f'Encrypted message is : {C}')

#decryption
M = pow(C, d)
M = math.fmod(M, n)
print(f'Original message is : {M}')