
for num in range(3, 21):
    result = f'{num} - '
    for x in range(1, num):
        for y in range(x + 1, num):
            if num % (x+y) == 0:
                result += f'{x}{y}'
    print(result)