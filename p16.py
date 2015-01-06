# Problem 16 Power digit sum:
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?


import os


def main():
  number = str(2**1000)
  digit_sum = 0
  for n in number:
    digit_sum += int(n)

  print digit_sum
  return


main()
