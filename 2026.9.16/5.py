def count_char(s, ch):
    a = 0
    for i in s:
        if i == ch:
            a += 1
    return a
print(count_char("hello world", "l"))
