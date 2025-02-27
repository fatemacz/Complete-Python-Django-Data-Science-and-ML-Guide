class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email


class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author


class Forum:
    def __init__(self):
        self.users = []
        self.posts = []

    def register_user(self, username: str, email: str):
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, title: str, content: str, author: User):
        post = Post(title, content, author)
        self.posts.append(post)
        return post

    def find_user_by_username(self, username: str):
        for user in self.users:
            if user.username == username:
                return user

    def find_user_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user

    def find_posts_by_author(self, author: User):
        found_posts = []
        for post in self.posts:
            if post.author == author:
                found_posts.append(post)
        return found_posts


forum = Forum()

aye = forum.register_user("Aye123", "aye@gmail.com")
alice = forum.register_user("alice643", "a@a.com")

print(forum.users)

forum.create_post("My first post", "Post content", aye)

print(forum.posts)
# Now you should NOT search for posts like that. Use find_posts_by_author!
# print(forum.posts[0].title)
# print(forum.posts[0].content)
# print(forum.posts[0].author.username)
# print(forum.posts[0].author.email)

print(forum.find_user_by_username("admin12"))  # None
print(forum.find_user_by_username("Aye123").email)  # b@gmail.com

forum.create_post("Second great post", "Post content", aye)

# Find posts of the user
found_posts = forum.find_posts_by_author(aye)
found_posts_titles = [post.title for post in found_posts]
print(found_posts_titles)


# Find user by email and find all posts by that user
user_email = "b@gmail.com"
found_user = forum.find_user_by_email(user_email)
if found_user:
    print(forum.find_posts_by_author(found_user))
else:
    print(f"User with email {user_email} doesn't exist!")
