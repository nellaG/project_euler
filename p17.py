# Problem 17 Number letter counts
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
# 20 letters. The use of "and" when writing out numbers is in compliance
# with British usage.


def main():
  length = 0
  for i in range(1, 1001):
    num =(num_to_word_wrapper(i))
    length = length + len(str(num))
  print length


def num_to_word_wrapper(number):
  word = ''
  k = num_to_word(number, word)
  return k


def num_to_word(number, word):

  if number % 1000 != number:
    digit = digit_to_word(number / 1000)
    word = word + digit + 'thousand'
    return num_to_word(number % 1000, word)
  elif number % 100 != number:
    digit = digit_to_word(number / 100)
    word = word + digit + 'hundred' + ('and' if number % 100 != 0 else '')
    return num_to_word(number % 100, word)
  elif number % 10 != number:
    digit = digit_to_word(number / 10)
    if digit != 'one':
      word = word + (digit if number >= 100 else '') + print_to_ten(number / 10)
    else:
      # eleven, twelve, thirteen, fourteen, ...
      tenth = digit_to_tenth(str(number % 10))
      word = word + tenth
      return word
    return num_to_word(number % 10, word)
  else:
    digit = digit_to_word(str(number))
    word = word + digit
    return word


def digit_to_word(digit):
  return {
      '0': '',
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

def print_to_ten(digit):
  return {
      '0': '',
      '2': 'twenty',
      '3': 'thirty',
      '4': 'fourty',
      '5': 'fifty',
      '6': 'sixty',
      '7': 'seventy',
      '8': 'eighty',
      '9': 'ninty',
  }[str(digit)]

def digit_to_tenth(digit):
  return {
      '0': 'ten',
      '1': 'eleven',
      '2': 'twelve',
      '3': 'thirteen',
      '4': 'fourteen',
      '5': 'fifteen',
      '6': 'sixteen',
      '7': 'seventeen',
      '8': 'eighteen',
      '9': 'nineteen',
  }[str(digit)]

main()
