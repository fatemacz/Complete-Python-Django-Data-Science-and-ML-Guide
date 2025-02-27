"""
Ref: https://www.w3schools.com/python/python_ref_keywords.asp

Python has a set of keywords that are reserved words that cannot be used as variable names, function names, or any other identifiers:

Keyword	    Description
-------------------------------------------------------------------------------------------------------------------
and	        A logical operator
as	        To create an alias
assert	    For debugging
break	    To break out of a loop
class	    To define a class
continue	To continue to the next iteration of a loop
def	        To define a function
del	        To delete an object
elif	    Used in conditional statements, same as else if
else	    Used in conditional statements
except	    Used with exceptions, what to do when an exception occurs
False	    Boolean value, result of comparison operations
finally	    Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for	        To create a for loop
from	    To import specific parts of a module
global	    To declare a global variable
if	        To make a conditional statement
import	    To import a module
in	        To check if a value is present in a list, tuple, etc.
is	        To test if two variables are equal
lambda	    To create an anonymous function
None	    Represents a null value
nonlocal	To declare a non-local variable
not	        A logical operator
or	        A logical operator
pass	    A null statement, a statement that will do nothing
raise	    To raise an exception
return	    To exit a function and return a value
True	    Boolean value, result of comparison operations
try     	To make a try...except statement
while	    To create a while loop
with	    Used to simplify exception handling
yield	    To return a list of values from a generator
"""

# # The del keyword is used to delete objects.
# # In Python everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list etc.
# list1 = [1, 2, 3]
# print(list1)
# del list1[1]
# print(list1)


def validate_grade(fn):
    def wrapper(*args, **kwargs):
        grade = args[0] if args else kwargs.get("grade", None)

        if grade not in ["A+", "A", "A-", "B+", "B", "B-", "C"]:
            raise ValueError(f"Invalid Grade: {grade}")
        else:
            print(f"Valid Grade: {grade}")
        return fn(*args, **kwargs)

    return wrapper


@validate_grade
def get_grade_point(grade):
    return (
        9
        if grade == "A+"
        else (
            8
            if grade == "A"
            else (
                7
                if grade == "A-"
                else (
                    6
                    if grade == "B+"
                    else 5 if grade == "B" else 4 if grade == "B-" else 0
                )
            )
        )
    )


def validate_gpa(fn):
    def wrapper(*args, **kwargs):
        grade_point_average = (
            args[0] if args else kwargs.get("grade_point_average", None)
        )

        if grade_point_average < 0 or grade_point_average > 9:
            raise ValueError(f"Invalid GPA: {grade_point_average}")
        else:
            print(f"Your GPA is {grade_point_average}!")
        return fn(*args, **kwargs)

    return wrapper


@validate_gpa
def describe_grade(grade_point_average):
    if grade_point_average >= 7:
        return "First Class Honours"
    elif grade_point_average >= 5.5:
        return "Second Class, First Division"
    elif grade_point_average >= 4.0:
        return "Second Class, Second Division"
    else:
        return "Third Class"


def get_honours_level(*args, **kwargs):
    subject_count = len(args)
    total_grade_points = 0

    for grade in args:
        total_grade_points += get_grade_point(grade)

    name = kwargs.get("name", "Student")
    course = kwargs.get("course", "Master of IT")
    university = kwargs.get("university", "University of Auckland")

    grade_point_average = total_grade_points / subject_count
    result = describe_grade(grade_point_average)

    return f"Congratulations, {name}!\nYou achieved '{result}' in your {course} at the {university}."


try:
    print(get_honours_level("B+", "A", "A", "A+", name="Aye"))
except Exception as e:
    print(e)
