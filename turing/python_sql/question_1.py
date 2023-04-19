class Turing:
    def __int__(self):
        self.data = "welcome"

    def hello(self, name):
        print(self.data + name)


obj = Turing()
obj.hello("Turing")
