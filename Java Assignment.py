def fibonacci(count):
    sequence = []
    d, c = 0, 1

    for _ in range(count):
        sequence.append(d)
        d, c = c, d + c

    return sequence


numbers = fibonacci(100)

for position, value in enumerate(numbers, start=1):
    print(f"{position}: {value}")