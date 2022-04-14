#!/usr/bin/env python3

"""
This module contains functions to
"""

import csv
import re

__author__ = 'Matthew Meyer and Michael Fowler'
__version__ = '1.0'
__copyright__ = "Copyright 2022.04.12, Regular Expressions"
__github__ = "https://github.com/mattdotpy/RegEx.git"

valid_files = 0
invalid_files = 0


def valid_data():
    global valid_files, invalid_files

    with open("input", newline='') as file, open("invalid", "w", newline='') as invalid, \
            open("valid", "w", newline='') as valid:

        reader = csv.reader(file, delimiter="|")
        for row in reader:
            try:
                id, name, email, phone = row
                name = name.split(', ')
            except:
                writer = csv.writer(invalid)
                writer.writerow([row])
                invalid_files = invalid_files + 1

            error_code = ''
            try:
                id == int(id)
                # writer = csv.writer(valid)
                # writer.writerow([id, name, email, phone])
            except:
                error_code += 'I'


            pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(edu)'
            i = re.search(pattern, email)
            if i == None:
                error_code += '+E'
            else:
                print()
                # writer = csv.writer(valid)
                # writer.writerow([id, name, email, phone])


            pattern3 = '[a-zA-Z]'
            y = re.search(pattern3, str(name))
            if y == None:
                error_code += '+N'
            else:
                print()
                # writer = csv.writer(valid)
                # writer.writerow([id, name, email, phone])

            pattern2 = '(\d\d\d)+\.(\d\d\d)+\.(\d\d\d\d)'
            j = re.search(pattern2, phone)
            if j == None:
                error_code += '+P'
            else:
                print()
                # writer = csv.writer(valid)
                # writer.writerow([id, name, email, phone])

            # writer = csv.writer(valid)
            # writer.writerow([row])
            # valid_files += 1


def write_valid():
    global valid_files

    with open("valid", "w", newline='') as valid:
        writer = csv.writer(valid)
        # writer.writerow([row])
        valid_files += 1

    '''finally:
    print(f'This is the number of valid data: {valid_files}')
    print()
    print(f'This is the number of invalid data: {invalid_files}')
    print()'''


def write_invalid():
    global invalid_files

    with open("invalid", "w", newline='') as invalid:
        writer = csv.writer(invalid)
        # writer.writerow([row])
        invalid_files = invalid_files + 1


def main():
    valid_data()


if __name__ == '__main__':
    main()
