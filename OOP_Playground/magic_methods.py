class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"

u = User("Ana")
print(u)        


class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

l = MyList([1, 2, 3])
print (len(l))

class Number:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value 

n1 = Number(30)
n2 = Number(20)

print(n1 == n2)
