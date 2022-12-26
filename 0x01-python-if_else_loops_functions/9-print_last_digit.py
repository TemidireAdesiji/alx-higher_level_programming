#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        digitals = number % 10
    else:
        digitals = number % -10
        digitals *= -1

        print("{:d}".format(digitals), end='')
        return (digitals)
