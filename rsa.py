import math

#taking input from user
p = int(input('Input a prime number as p: '))
q = int(input('Input a prime number as q: '))

#checking user input whether those prime or not
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

#calculating n and phi_n
n = p * q
phi_n = (p-1) * (q-1)

print(f'n = {n} and phi_n = {phi_n}')

#calculating public key (e)
for i in range(2, phi_n):
    if math.gcd(i, phi_n) == 1:
        e = i
        break

#calculating private key (d)
j = 0
while True:
    if (j * e) % phi_n == 1:
        d = j
        break
    j += 1

print(f'private key is = {d}')
print(f'public key is = {e}')

#taking input for message
msg = int(input('Input your integer message: '))

#encryption
C = (msg ** e) % n
print(f'Encrypted message is : {C}')

#decryption
M = (C ** d) % n
print(f'Original message is : {M}')