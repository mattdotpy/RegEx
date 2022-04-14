#!/usr/bin/env python3

"""
This module contains functions to
"""

import sys
import csv
import re

__author__ = 'Matthew Meyer and Michael Fowler'
__version__ = '1.0'
__copyright__ = "Copyright 2022.04.12, Regular Expressions"
__github__ = "https://github.com/mattdotpy/RegEx.git"

from _csv import writer
valid_files = 0
invalid_files = 0


def valid_data():
    global valid_files, invalid_files

    with open("input", newline='') as file, open("invalid", "w", newline='') as invalid, \
            open("valid", "w", newline='') as valid:

        reader = csv.reader(file, delimiter=",")
        for row in reader:

            try:
                id, l_name, f_name, email, phone = row
                pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(edu)'
                x = re.search(pattern, email)
            except:
                print(f'+E {x}')

            try:
                pattern2 = '(\d\d\d).(\d\d\d).(\d\d\d\d)'
                re.search(pattern2, phone)
            except:
                print('+P')

            try:
                pattern3 = '[a-zA-Z]'
                re.search(pattern3, l_name)
                re.search(pattern3, f_name)
            except:
                print('+N')

            try:
                pattern4 = '[0-1000]'
                re.search(pattern4, id)
            except:
                print('+I')
            try:
                writer = csv.writer(valid)
                writer.writerows([row])
                valid_files += 1
            except:
                writer = csv.writer(invalid)
                writer.writerows([row])
                invalid_files = invalid_files + 1
            finally:
                print(f'This is the number of valid data: {valid_files}')
                print()
                print(f'This is the number of invalid data: {invalid_files}')


def invalid_data():
    print()


def main():
    valid_data()


if __name__ == '__main__':
    main()
