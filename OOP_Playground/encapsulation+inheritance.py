class BankAccount:
    def __init__(self, ballance):
        self._ballance = ballance

    def deposit(self, amount):
        self._ballance += amount

    def get_ballance(self):
        print(self._ballance)


b1 = BankAccount(2000)
b1.deposit(3000)
b1.get_ballance()             


class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.name}"

class Admin(User):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role

    def delete_user(self):
        return "User deleted"

admin = Admin("Alex","admin")
print(admin.greet())
print(admin.delete_user())        