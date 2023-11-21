import calendar
import datetime
import re

# Get the current year and month
current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day
calendar.setfirstweekday(3)

# Create regular expression patterns
gday = r'\b{current_year}\b'.format(current_year=current_year)
gnight = r"\033[32m\033[1m{current_year}\033[0m".format(current_year=current_year)
gdayg = r'\b{current_day}\b'.format(current_day=current_day)
gnightg = r"\033[32m\033[1m{current_day}\033[0m".format(current_day=current_day)

# Replace the current year and date with green colored coloured date
cal_text = calendar.month(current_year, current_month)
cal_text = re.sub(gday, gnight, cal_text)
cal_text = re.sub(gdayg, gnightg, cal_text)

print(cal_text)
