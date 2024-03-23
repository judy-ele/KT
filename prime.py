import sys
def is_prime(n):
    if n < 2:
        return False
    if(n>sys.maxsize): return 'Out of range'
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input('Enter number: '))
print(is_prime(n))
