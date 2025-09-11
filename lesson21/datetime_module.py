from datetime import datetime
import pytz

row1 = "2024-11-30 17:40:55" #UTC (ISO)
row2 = "24-17-03T5:55:55 PM"
row3 = "28/02/20 8:50:31.260 -0200" #TZ -2 hours

row1_transformed = datetime.fromisoformat(row1) #працює бо iso формат
# row2_transformed = datetime.fromisoformat(row2) # не працює
row2_transformed = datetime.strptime(row2, "%y-%d-%mT%I:%M:%S %p")
row3_transformed = datetime.strptime(row3, "%d/%m/%y %H:%M:%S.%f %z")
# print(datetime.strftime(row2_transformed, "%d/%m/%Y, %H:%M:%S"))
# print(row2_transformed.time())

print(row3_transformed.tzinfo)
print(row3_transformed.tzname())
print(row3_transformed)
print(datetime.now(pytz.timezone("Europe/Kyiv")))
print(datetime.now())