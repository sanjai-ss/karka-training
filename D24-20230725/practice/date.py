# from datetime import date
# curr_date=date(11,7,23)
# curr_date=date.today().year
# print(curr_date)

# from datetime import time
# curr_time=time(11,12,13)
# curr_time=curr_time.minute
# print(curr_time)


from datetime import datetime
curr_datetime=datetime(2020,5,6,11,12,13)
# curr_datetime=datetime.today().hour
# curr_datetime=curr_datetime.month
# curr_datetime=datetime.today()
# print(curr_datetime)
curr_datetime=datetime.now()
curr_datetime=curr_datetime.strftime("%D")
print(curr_datetime)