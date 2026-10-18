class Counter:
    def __init__(self, count):
        self.count = count = 0
    def add(self):
        self.count += 1
    def get(self):
        return self.count
c = Counter(0)
c.add()
c.add()
print(c.get())

        
    
