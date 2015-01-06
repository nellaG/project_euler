# Problem 17 Number letter counts
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
# 20 letters. The use of "and" when writing out numbers is in compliance
# with British usage.


import os


def main():
  for i in range(1, 11):
    print i
  num_to_word(1000)


def num_to_word(number):
  word = ''

  if number % 1000 != number:
    digit = digit_to_word(number / 1000)
    print digit + ' thousand'
  elif number % 100 != number:
    pass
  elif number % 10 != number:
    pass
  else:
    pass


def digit_to_word(digit):
  return {
      '0': 'zero',
      '1': 'one',
      '2': 'two',
      '3': 'three',
      '4': 'four',
      '5': 'five',
      '6': 'six',
      '7': 'seven',
      '8': 'eight',
      '9': 'nine'
  }[str(digit)]


main()
