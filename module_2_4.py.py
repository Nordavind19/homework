numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    marker = True
    for factor in range(2, num):
        if num % factor == 0:
            marker = False
            not_primes.append(num)
            break
    if marker == True and num != 1:
        primes.append(num)
print('Primes:', primes)
print('Not primes:', not_primes)








