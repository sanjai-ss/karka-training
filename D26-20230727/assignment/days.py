from datetime import datetime
from datetime import timedelta
d=int(input("type a number"))
# print(datetime.date.today())
my_date="27july2023"
today=datetime.strptime(my_date,"%d%B%Y")
day=today + timedelta (days=d)
print(day)

