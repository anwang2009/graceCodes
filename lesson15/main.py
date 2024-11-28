"""
Lesson 15: Classes
"""


class Pet:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("my name is", self.name)



if __name__ == "__main__":
    p = Pet()
    p.talk()

