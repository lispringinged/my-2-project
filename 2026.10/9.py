from collections import deque
p = deque()
p.append(1)
p.append(2)
p.append(3)
while p:
    print(p.popleft())