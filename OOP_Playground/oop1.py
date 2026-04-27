class User:
    pass


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}"    

u1 = User("Ana", 25)
u2 = User("Alex",30)

print(u1.greet())