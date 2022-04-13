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

            try:
                id


def invalid_data():
    print()


def main():
    valid_data()


if __name__ == '__main__':
    main()
