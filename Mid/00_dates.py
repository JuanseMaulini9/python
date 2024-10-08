### Dates ###

from datetime import datetime

def print_date(date):
  print(date.day)
  print(date.month)
  print(date.year)
  print(date.hour)
  print(date.minute)
  print(date.second)
  print(date.timestamp())

now = datetime.now()

print_date(now)

year_2025 = datetime(2025,1,1)

print_date(year_2025)

from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.day)
print(current_date.month)
print(current_date.year)

current_date = date(2024,9,9)

print(current_date.day)
print(current_date.month)
print(current_date.year)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)

dif = year_2025 - now
print(dif)
dif = year_2025.date() - current_date
print(dif)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)


