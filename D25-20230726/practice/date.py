from datetime import datetime
date_str="24December2022"
print(datetime.strptime(date_str,"%d%B%Y"))

from datetime import datetime
from datetime import timedelta
date_str="24December2022"
date=datetime.strptime(date_str,"%d%B%Y")
end_date=date + timedelta (days=5)
print(end_date) 