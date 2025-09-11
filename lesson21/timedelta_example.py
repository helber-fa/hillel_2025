from datetime import datetime,timedelta
url = f"somesite.com/api/v2?filterStart=;filterEnd="
today = datetime.now()
print(today)

seven_days_ago = today - timedelta(days=7, hours=5)
five_minutes_ago = today - timedelta(minutes=30)
print(seven_days_ago)

url = f"somesite.com/api/v2?filterStart={five_minutes_ago};filterEnd={today}"
print(url)