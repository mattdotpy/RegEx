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

from _csv import writer
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
            except:
                writer = csv.writer(invalid)
                writer.writerow([row])
                invalid_files = invalid_files + 1

            error_code = ''
            try:
                id = int(id)
            except:
                error_code += 'I'

            try:
                pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(edu)'
                i = re.search(pattern, email)
                if i == None:
                    print(f'+E')
                else:
                    pass
            except:
                error


                pattern3 = '[a-zA-Z]' + '[,]' + '[a-zA-Z]'
                y = re.search(pattern3, name)
                if y == None:
                    print('+N')
                else:
                    pass

                pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(edu)'
                i = re.search(pattern, email)
                if i == None:
                    print(f'+E')
                else:
                   pass

                pattern2 = '(\d\d\d).(\d\d\d).(\d\d\d\d)'
                j = re.search(pattern2, phone)
                if j == None:
                    print('+P')
                else:
                    pass

                writer = csv.writer(valid)
                writer.writerow([row])
                valid_files += 1



def write_valid():
    global valid_files

    with open("valid", "w", newline='') as valid:
        writer = csv.writer(valid)
        writer.writerow([row])
        valid_files += 1

    '''finally:
    print(f'This is the number of valid data: {valid_files}')
    print()
    print(f'This is the number of invalid data: {invalid_files}')
    print()'''

def write_invalid():
    global invalid_files

    with open ("invalid", "w", newline='') as invalid:
        writer = csv.writer(invalid)
        writer.writerow([row])
        invalid_files = invalid_files + 1




def main():
    valid_data()


if __name__ == '__main__':
    main()
