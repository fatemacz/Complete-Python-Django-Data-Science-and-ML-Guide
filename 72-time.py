import time

# 1. time and ctime
current_time_in_seconds = time.time()
# print(time.ctime(current_time_in_seconds))

print(time.ctime(23423423423))


# 2. sleep
start_time = time.time()
print('Start:', start_time)

time.sleep(3)

end_time = time.time()
print('Continue:', end_time)

print('Time spent:', end_time - start_time)


# 3. Measure time
start_time = time.time()

my_list = list(range(100_000_000))
print(my_list[1000000])

end_time = time.time()

print('Time spent:', round(end_time - start_time, 2))
