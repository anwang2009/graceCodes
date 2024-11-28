"""
Lesson 15: Classes
"""

class Pet:
    def __init__(self, name):
        self.name = name
        self.count = 0

    def talk(self):
        print("My name is", self.name, end = ".\n")
        self.count += 1

    def getCount(self):
        print(self.count)


if __name__ == "__main__":
    p = Pet("Grace")
    p.talk()
    p.getCount()

