# 1. Syntax of the decorator function
def decorator_function(original_fn):
    def wrapper_function(*args, **kwargs):
        print(args)
        print(kwargs)
        # Some actions before execution of the original_fn function
        print("Executed before function")

        result = original_fn(*args, **kwargs)

        # Some actions after execution of the original_fn function
        print("Executed after function")

        return result

    return wrapper_function


@decorator_function
def my_function(*args, **kwargs):
    print("This is my function")


my_function(10, name='Bogdan')


# 2. Checking if user is authenticated in the decorator function
def is_user_authenticated():
    return True


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            print("User is authenticated!")
            return fn(*args, **kwargs)
        else:
            raise Exception("User is not authenticated")

    return wrapper


@check_user_auth
def do_sensitive_job():
    # Perform action only if user is authenticated
    print("Some sensitive job results")


do_sensitive_job()


# 3. Logging in the decorator function
def log_function_call(fn):
    def wrapper(*args, **kwargs):
        print(f"Calling function {fn.__name__}")
        print(f"Function arguments: {args}, {kwargs}")
        res = fn(*args, **kwargs)
        print(f"Result of the function is {res}")
        return res

    return wrapper


@log_function_call
def mult_numbers(a, b):
    return a * b


print(mult_numbers(10, 2))
print('')


@log_function_call
def sum_numbers(a, b):
    return a + b


print(sum_numbers(10, 2))
print('')
print(sum_numbers(a=50, b=5))


# 4. Arguments validation in the decorator function
def validate_args(fn):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("Arguments must be integers!",
                                 f"{arg} is of type {type(arg)}")
        return fn(*args, **kwargs)

    return wrapper


@validate_args
def sum_nums(a, b):
    return a + b


try:
    print(sum_nums(5, 2))
    print(sum_nums('5', 2))
except ValueError as e:
    print(e)
