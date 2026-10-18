class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name + "在叫")
a = Animal("猫")
a.speak()