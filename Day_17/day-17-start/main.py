class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User("12","Kanishka")
user_2 = User("13", "Jack")

user_1.follow(user_2)
print(f"{user_1.username} has/have {user_1.follower} followers")
print(f"{user_1.username} has/have {user_1.following} following")
print(f"{user_2.username} has/have {user_1.follower} followers")
print(f"{user_2.username} has/have {user_1.following} following")