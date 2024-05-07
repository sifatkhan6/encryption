p = int(input('Inplut a prime number as p: '))
q = int(input('Inplut a prime number as q: '))

n = p*q
phi_n = (p-1) * (q-1)

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, num**0.5+1):
        if num % i == 0:
            return False
    return True

if check_prime(p):
    print(f"{p} is a prime number")
else:
    print(f"{p} is not a prime number")