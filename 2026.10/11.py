class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def say_hi(self):
        print("我是" + self.name)
s = Student('小明', 90)
print(s.name)
print(s.score)
s.say_hi()