p = int(input('Input a prime number as p: '))
q = int(input('Input a prime number as q: '))

n = p*q
phi_n = (p-1) * (q-1)

def check_prime(num):
    if num <= 1:
        print(f'{num} is not a prime number')
        new_num = int(input(f'Input a prime number replace of {num}: '))
        num = new_num
        return num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f'{num} is not a prime number')
            new_num = int(input(f'Input a prime number replace of {num}: '))
            return new_num
        break
    else:
        print(f'{num} is a prime number')

new_input = check_prime()

check_prime(p)
check_prime(q)

