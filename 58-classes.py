# 1. Methods are inherited by the instances of the class
class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car stopped")


my_car = Car()
print(type(my_car))
print(isinstance(my_car, Car))
print(isinstance(my_car, object))
print(dir(my_car))
print(my_car.__dict__)

my_car.move()
my_car.stop()


# 2. Magic __init__ method
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def info(self):
        print(f"User {self.username} has email {self.email}")


first_user = User("Aye123", "aye@gmail.com")
first_user.info()
print(first_user.username)
print(first_user.email)

other_user = User("alice2345", "alice@gmail.com")
other_user.info()
print(other_user.username)
print(other_user.email)
print(other_user.__dict__)

other_user.username = "a6363"
print(other_user.username)

# # not good practice. just for demonstration
# other_user.address = "123 Main St"
# print(other_user.address)
# print(other_user.__dict__)


# 3. Methods
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.likes_qty = 0

    def like(self):
        self.likes_qty += 1


my_post = Post("My first post", "Some post content", "Aye")
print(my_post)
print(my_post.title)
print(my_post.likes_qty)

my_post.like()  # recommended
my_post.like()
print(my_post.likes_qty)

Post.like(my_post)  # not recommended, just for demonstration
print(my_post.likes_qty)


# Post class doesn't have such attributes!
# Post.likes_qty
# Post.title


# 4. Static methods
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.likes_qty = 0

    def like(self):
        self.likes_qty += 1

    @staticmethod
    def format_post(title, content):
        return f"Post title: {title}\n" f"Post content: {content}"


formatted_post = Post.format_post("Some post title", "Post contents")  # recommended
print(formatted_post)
print(type(formatted_post))

# # not recommended for static methods, also not possible without @staticmethod decorator
# my_post = Post("My first post", "Some post content", "Aye")
# formatted_post = my_post.format_post("Some post title", "Post contents")
# print(formatted_post)


# 5. Class with just static methods
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def mult(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        raise ValueError("Can't divide by zero")


print(Calculator.add(20, 10))
print(Calculator.subtract(20, 10))
print(Calculator.mult(20, 10))
print(Calculator.divide(20, 10))


# 6. Class attributes
class User:
    users_qty = 0  # class attribute

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.users_qty += 1


first_user = User("bob234", "bob@bob.com")
print(f"first_user.users_qty: {first_user.users_qty}")
print(f"User.users_qty: {User.users_qty}")
print()

second_user = User("alice356", "alice@alice.com")
print(f"second_user.users_qty: {second_user.users_qty}")
print(f"User.users_qty: {User.users_qty}")
print(second_user.__dict__)  # users_qty is not in the instance dictionary
print(User.__dict__)  # users_qty is in the class dictionary
print()

third_user = User("john324", "john@john.com")
print(f"third_user.users_qty: {third_user.users_qty}")
print(f"User.users_qty: {User.users_qty}")
print()

print("Assigning users_qty of 10 to third_user")
third_user.users_qty = 10
print(f"User.users_qty: {User.users_qty}")  # 3
print(f"third_user.users_qty: {third_user.users_qty}")  # 10
print(third_user.__dict__)  # users_qty is now in the instance dictionary


# 7. Magic methods
class Post:
    def __init__(self, title):
        self.title = title

    def __add__(self, other):
        return f"{self.title} {other.title}"

    def __eq__(self, other):
        return self.title == other.title


first_post = Post("This is first post.")
second_post = Post("This is second post.")
same_post_as_first = Post("This is first post.")

print(first_post + second_post)

print(first_post == same_post_as_first)  # True
print(first_post == second_post)  # False


# 8. Class extension
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        return print(f"User {self.username} is logged in!")


class AdminUser(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        self.role = role
        self.is_admin = True

    def approve_post(self):
        return print("Post approved!")

    # def __str__(self):
    #     return f"User {self.username} has email {self.email}"


my_admin = AdminUser("admin123", "admin@admin.com", "Administrator")
print(my_admin)
my_admin.login()  # from parent class: User
my_admin.approve_post()  # from AdminUser class

print(type(my_admin))
print(isinstance(my_admin, AdminUser))
print(isinstance(my_admin, User))
print(isinstance(my_admin, object))

print(my_admin.__dict__)

my_user = User("bob234", "bob@bob.com")

print(my_user.__dict__)

print(User.__subclasses__())  # [<class '__main__.AdminUser'>]
print()

print(object.__subclasses__())
