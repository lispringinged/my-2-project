# %%
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    def average(self):
        return sum(self.scores) / len(self.scores)
s = Student("小明", [80, 90, 100])
print(s.average())
# %%
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def get_balance(self):
        return self.balance
b = BankAccount("小王", 100)
b.deposit(50)
print(b.get_balance())
# %%
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("你好，我是" + self.name)
p = Person("李雷")
p.greet()
# %%
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h 
    def perimeter(self):
        return 2 * (self.w + self.h)
    def describe(self):
        print(f"面积是 {self.area()}，周长是 {self.perimeter()}")
r = Rectangle(4, 5)
r.describe()
# %%
class Circle:
    def __init__(self, r):
        self.r = r
    def diameter(self):
        return 2 * self.r
    def info(self):
        print(f"直径是{self.diameter()}")
c = Circle(5)
c.info()
# %%
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    def __str__(self):
        return f"{self.name}, {self.scores}分"
s = Student("小明", 90)
print(s)
#%%
class Chat:
    def __init__(self):
        self.messages = []
    def add(self,msg):
        self.messages.append(msg)
    def last(self):
        return self.messages[-1] if self.messages else None
c = Chat()
c.add("你好")
c.add("再见")
print(c.last())
# %%
class Counter:
    def __init__(self):
        self.count = 0
    def add(self):
        self.count += 1
    def __str__(self):
        return f"当前计数:{self.count}"
c = Counter()
for _ in range(3): 
    c.add()
print(c)
#%%
class ShoppingCart:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def total(self):
        return len(self.items)
cart = ShoppingCart()
cart.add("apple")
cart.add("banana")
print(cart.total())
# %%
class ScoreList:
    def __init__(self, name):
        self.name = name
        self.list = []
    def add(self, s):
        self.list.append(s)
    def average(self):
        return sum(self.list) / len(self.list) if self.list else 0
s1 = ScoreList("小明")
a = [80, 90, 100]
for items in a:
    s1.add(items)
print(s1.average())
# %%
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"《{self.title}》-{self.author}"
b = Book("三体", "刘慈欣")
print(b)
# %%
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return f"{self.name} 汪汪"
class Person:
    def __init__(self, name):
        self.name = name
    def adopt(self, dog):
        self.dog = dog
    def play(self):
        return self.dog.bark()
p = Person("小明")
d = Dog("小黑")
p.adopt(d)
print(p.play())
# %%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
p = Point(3, 4)
print(p)

# %%
class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []
    def add_score(self, score):
        self.scores.append(score)
    def get_average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0
s = Student("小明")
s.add_score(80)
s.add_score(90)
s.add_score(100)
print(s.get_average())

# %%
class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []
    def __str__(self):
        scores_text = "、".join(str(score) for score in self.scores)
        return f"{self.name}:成绩{scores_text}"
    def add_score(self, score):
        self.scores.append(score)
class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def __str__(self):
        names = [student.name for student in self.students]
        names2 = (",".join(names))
        return f"{self.name}:{names2}"
a = Classroom("一班")
b = Student("小明")
c = Student("小红")
a.add_student(b)
a.add_student(c)
print(a)
s = Student("小明")
s.add_score(95)
print(s)    #26.10.22 20.32这个写了好久，刚换到gpt，感觉自己是傻逼
# %%
import json
student = {
    "name": "小明",
    "score": 95
}
text = json.dumps(student, ensure_ascii=False)
result = json.loads(text)
print(result["name"])
print(type(result))
# %%
