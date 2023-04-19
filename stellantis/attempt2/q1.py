class Food:
    def __init__(self):
        self.name = 'F'
        self.origin = 'E'

    def say(self):
        print("Food"+self.name)

class Drink:
    def __init__(self):
        self.name = 'D'
        self.origin = 'A'

    def say(self):
        print("Drink"+self.name)

class X(Food, Drink):
    pass

x = X()
x.name = 'Apple'
x.say()
print(x.origin)