class User:
    count = 0

    def __init__(self, name, login, password):
        self._name = name
        self._login = login
        self._password = password
        User.count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def set_password(self, value):
        self._password = value

    password = property(fset=set_password)

    @property
    def login(self):
        return self._login

    def show_info(self):
        return f'Login: {self._login}, Name: {self._name}'

class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self._role = role
        User.count -= 1
        SuperUser.count += 1

    @property
    def role(self):
        return self._role

    @role.setter
    def name(self, value):
        self._role = value

    def show_info(self):
        return super().show_info() + f', role:{self._role}'



user1 = User('Paul Mccarty', 'Paul', '1234')
user2 = User('George Harrison', 'George', '5678')
user3 = User('Ringo  Star', 'Ringo', '3423')
user4 = SuperUser('John Lenon', 'John', '3674', 'admin')

print(f'Users count {User.count}')
print(f'Superusers count {SuperUser.count}')

print(user1.name)
user2.name = 'Ringo Star'
print(user2.name)

print(user4.role)

user2.set_password = 'Ri'
print(user2.password)
print(user2.login)
user2.login = '2323'

