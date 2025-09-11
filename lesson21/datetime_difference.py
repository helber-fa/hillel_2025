import time
from datetime import datetime
import pytz

server_time = "2025-09-09 20:26:10.22633 +00:00"
client_time = "2025-09-09 20:26:10.22633"

client_time_dt = datetime.strptime(client_time, "%Y-%m-%d %H:%M:%S.%f")
server_time_dt = datetime.strptime(server_time, "%Y-%m-%d %H:%M:%S.%f %z")

client_time_dt2 = pytz.timezone("Europe/Kyiv").localize(client_time_dt)

print(client_time_dt)
print(client_time_dt2)
print(server_time_dt)
print(type(client_time_dt2))

local_time_zone = time.timezone
print(local_time_zone)
# client_time_dt2 = pytz.timezone(local_time_zone).localize(client_time_dt)
# print("_"*80)
# print(client_time_dt)
# print(client_time_dt2)
# print(server_time_dt)
# print(type(client_time_dt2))

diff_in_time = server_time_dt - client_time_dt2
print(diff_in_time.seconds)
print(type(diff_in_time))
