import calendar
import datetime
import re

# Get the current year and month
current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day
calendar.setfirstweekday(2)

# Create regular expression patterns
prday = r'\b{current_year}\b'.format(current_year=current_year)
pnightr = r"\033[35m\033[1m{current_year}\033[0m".format(current_year=current_year)
pdayr = r'\b{current_day}\b'.format(current_day=current_day)
prnight = r"\033[35m\033[1m{current_day}\033[0m".format(current_day=current_day)

# Replace the current year and date with pink colored coloured date
calendar_text = calendar.month(current_year, current_month)
calendar_text = re.sub(prday, pnightr, calendar_text)
calendar_text = re.sub(pdayr, prnight, calendar_text)

print(calendar_text)