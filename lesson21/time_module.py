import time

# print(time.time()) # кількість секунд з 1970 року
# print(time.localtime()) # віддає об'єкт часу
# current_time = time.localtime()
#
# print(current_time.tm_year)
# print(current_time.tm_mon)
# print(current_time.tm_mday)
# print(current_time.tm_zone)
# print(current_time.tm_hour)
#
# print(f"Now is {current_time.tm_hour}:{current_time.tm_min}")
#
current_time_in_sec = time.time()
#
# time.sleep(3.5)
#
# print(f"Difs in time: {time.time() -current_time_in_sec} seconds")


while time.time() - current_time_in_sec < 10:
    print("Waiting for element...")
    time.sleep(1)