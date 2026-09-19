d = {"cat": 1}
key = "banana"
if key not in d:
    d[key] = 1
else:
    d[key] += 1
print(d)