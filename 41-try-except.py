# 1. Different except blocks
try:
    salary = int(input("Enter salary amount: "))
    days_qty = int(input("Enter days quantity: "))
    salary_per_day = round(salary / days_qty)
    print(salary_per_day)
except ValueError:
    print("Cannot convert value to integer")
except ZeroDivisionError:
    print("Cannot divide by zero!")


# 2. One except block with different error types
try:
    salary = int(input("Enter salary amount: "))
    days_qty = int(input("Enter days quantity: "))
    salary_per_day = round(salary / days_qty)
    print(salary_per_day)
except (ValueError, ZeroDivisionError) as e:
    if type(e) == ValueError:
        print(e)
        print("Cannot convert value to int")
    if type(e) == ZeroDivisionError:
        print(e)
        print("Cannot divide by zero")


# 3. General exception class and different actions depending on the error type
try:
    salary = int(input("Enter salary amount: "))
    days_qty = int(input("Enter days quantity: "))
    salary_per_day = round(salary / days_qty)
    print(salary_per_day)
except Exception as e:
    if type(e) == ValueError:
        print(e)
        print("Cannot convert value to int")
    if type(e) == ZeroDivisionError:
        print(e)
        print("Cannot divide by zero")


# 4. General exception class
try:
    salary = int(input("Enter salary amount: "))
    days_qty = int(input("Enter days quantity: "))
    salary_per_day = round(salary / days_qty)
    print(salary_per_day)
except Exception as e:
    print(type(e))
    print(e)
    print(isinstance(e, Exception))
    print(isinstance(e, ValueError))
    print(isinstance(e, ZeroDivisionError))


# 5. No error context (NOT RECOMMENDED)
try:
    salary = int(input("Enter salary amount: "))
    days_qty = int(input("Enter days quantity: "))
    salary_per_day = round(salary / days_qty)
    print(salary_per_day)
except:
    print("Some error happened")


# 6. else and finally blocks
try:
    salary = int(input("Enter salary amount: "))
    days_qty = int(input("Enter days quantity: "))
    salary_per_day = round(salary / days_qty)
except ValueError as e:
    print(e)
    print("Cannot convert value to integer")
except ZeroDivisionError as e:
    print(e)
    print("Cannot divide by zero!")
else:
    print("Result, salary per day: ", salary_per_day)
finally:
    print("Salary operation calculation complete")


# 7. Handling file not found error
try:
    file = open("file.txt", "r")
except FileNotFoundError as e:
    print(e)
else:
    print("File is ready for reading")
finally:
    if 'file' in globals() and file and not file.closed:
        file.close()
        print("File was closed.")
        print(file.closed)
