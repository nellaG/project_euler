# Problem 13 Large Sum:
# Work out the first ten digits of the sum of the following
# one-hundred 50-digit numbers.


import os


def main():

  digits = ''
  large_sum = 0

  with open('p13file', 'r') as f:
    digits = f.read()
    f.close()
  digits_list = digits.split('\n')

  for digit_line in digits_list:
    large_sum += string_to_long_int(digit_line)

  print large_sum
  print '***************************************'
  return 


def string_to_long_int(digits):
  digits = digits[::-1]
  large_sum = 0
  i = 0
  for digit in digits:
    large_sum += int(digit) * (10 ** i)
    i += 1
  return large_sum


main()
