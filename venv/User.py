class User():
    def __init__(self,name,age):
        self.name=name
        self.age = age
        self.login_attempts = 0
    def describe_user(self):
        print(self.name.title() + " " + self.age)
    def show_attempts(self):
        print("Attempts: " + str(self.login_attempts))
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
class AnotherUser(User):
    def __init__(self,name,age):
        super().__init__(name,age)
stupiduser = AnotherUser('Joe','20')
print(stupiduser.describe_user())

my_user = User('marie', '19')
my_user.describe_user()
my_user.show_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.show_attempts()
my_user.reset_login_attempts()
my_user.show_attempts()
my_user.login_attempts = 23
my_user.show_attempts()