a = [10, 20, 30, 40, 50]
avg = sum(a)/len(a)
print(avg)

b = [5, 1, 4, 2, 8]
m = 5
for i in b:
    if i >= m:
        m = i
print(m)

c = [10, 20, 30, 40, 50]
print(c[2:])

d = [1, 2, 2, 3, 3, 3]
e = []
for i in d:
    if i not in e:
        e.append(i)
print(e)