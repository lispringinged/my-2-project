nums = [1, 2, 2, 3, 3, 3]
d = {}
for i in nums:
    if i not in d:
        d[i] = 0
    d[i] += 1  
print(d)