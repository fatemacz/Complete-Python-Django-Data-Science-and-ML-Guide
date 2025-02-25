# 1. date
from datetime import datetime, timedelta

future_date = datetime.date(2222, 9, 20)
print("Future date:", future_date)

print(future_date.year)
print(future_date.month)
print(future_date.day)


# 2. time
some_time = datetime.time(15, 30, 10)
print("Some time:", some_time)

print(some_time.hour)
print(some_time.minute)
print(some_time.second)


# 3. datetime
future_datetime = datetime(2100, 10, 12, 20, 50, 15)
print("Future date and time:", future_datetime)

print(dir(future_datetime))

print(future_datetime.hour)


# 4. strftime
future_datetime = datetime(2100, 10, 12, 20, 50, 15)
print("Future date and time:", future_datetime)

print("Formatted date:", future_datetime.strftime(
    "%B %d, %Y"))  # October 12, 2100
print("Formatted time:", future_datetime.strftime("%I:%M %p"))  # 08:50 PM
print("Formatted date and time:",
      future_datetime.strftime("%A, %B %d, %Y %I:%M %p"))  # Tuesday, October 12, 2100 08:50 PM
print("Formatted month:", future_datetime.strftime("%B"))  # October
print("Formatted year:", future_datetime.strftime("%Y"))  # 2100


# 5. strptime
formatted_datetime_str = "3000-11-20 14:25:45"

parsed_datetime = datetime.strptime(
    formatted_datetime_str, "%Y-%m-%d %H:%M:%S")
print(parsed_datetime)
print(parsed_datetime.year)

parsed_data = datetime.strptime("June 03, 2050", "%B %d, %Y")
print(parsed_data)
parsed_time = datetime.strptime("10:12 AM", "%I:%M %p")
print(parsed_time)
parsed_month = datetime.strptime("June", "%B")
print(parsed_month)
parsed_year = datetime.strptime("2222", "%Y")
print(parsed_year)


# 6. timedelta
future_datetime = datetime(2100, 12, 10, 18, 10, 45)

print("Original date:", future_datetime)

print(future_datetime + timedelta(days=100))
print(future_datetime + timedelta(hours=3))
print(future_datetime + timedelta(days=3, hours=5, minutes=15))

print(future_datetime - timedelta(days=5))
print(future_datetime - timedelta(days=365, hours=24))
