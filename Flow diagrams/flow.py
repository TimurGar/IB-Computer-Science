for y in range(10000):
    sum = 0
    for i in range(2, y):
        if y % i == 0:
            sum += i

    if y == sum + 1:
        print(y)
