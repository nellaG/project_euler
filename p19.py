# Problem 19 Counting Sundays
#
# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


# count the days which have thirty-one days: 1, 3, 5, 7, 8, 10, 12


# count the days which have thirty days: 4, 6, 9, 11

# february: a leap year occurs on any year which is divisible by 4: 1904, 1908, ...
# every leap year is in 20th century because every year is not divisible by 400 except 2000.
# -> 1 non-leap year, 24 leap years, 75 non-leap years

# should check if the year is leap year
month_table = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


week_table = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday',
    'friday', 'saturday']



leap_years = [year for year in range(1901, 2001) if year % 4 == 0 and
    (year % 400 == 0 or year % 100 != 0)]

tables = []
def func():
  count = 0

  for year in range(1901, 2001):
    for month in range(1, 13):
      if month_table[month-1] == 28 and year in leap_years:
        days = 29
      else:
        days = month_table[month-1]
      for day in range(1, days + 1):
        tables.append({'year': year, 'month': month, 'day': day})
  for day in range(len(tables)):
    if not (day - 6) % 7 and not tables[day]['day'] -1:
      count += 1
  return count

print func()


