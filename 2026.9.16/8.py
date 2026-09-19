words = ["a", "b", "a", "c", "a"]
d = {}
for i in words:
    if i not in d:
        d[i] = 0
    d[i] += 1
print(d)