class User:
    def __init__(self, user_id, username):
        print("New User is created.....")
        self.id = user_id
        self.username = username
        self.followers = 0

user_1 = User("001","mihir")


print(user_1.username)


