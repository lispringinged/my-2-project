class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(self.name + "汪汪")
d = Dog("小黑")
d.bark()