# Problem 20 Factorial digit sum
#
# n!means n * (n - 1) *...* 3 *2 * 1
#
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
#
# Find the sum of the digits in the number 100!


def get_digit(x):
  if x < 10 :
    return x
  else:
    return x % 10 + get_digit(int( x / 10))


def fac(x):
  if x == 1:
    return x
  else:
    return x * fac(x-1)

print '100!: ', fac(100)
print get_digit(fac(100))
