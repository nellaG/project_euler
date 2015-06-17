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


def thirty_one():
  return 31 * 7 * 100


def thirty():
  return 30 * 4 * 100

def leap_year_sum():
  return 28 * 76 + 29 * 24


print (thirty_one() + thirty() + leap_year_sum()) / 7

