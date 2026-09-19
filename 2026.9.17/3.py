def a(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total = total + i
    return total
print(a(10))


