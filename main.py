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

    with open("input_file", newline='') as file, open("invalid_file", "w", newline='') as invalid_file, \
            open("valid_file", "w", newline='') as valid_file:

        reader = csv.reader(file, delimiter="|")
        for row in reader:
            try:
                id, name, email, phone = row
                name = name.split(', ')
            except:
                error_code += '+L'
                writer = csv.writer(invalid_file)
                writer.writerow([row])
                writer.writerow([error_code])
                invalid_files = invalid_files + 1


            error_code = ''
            try:
                id == int(id)
                pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(edu)'
                i = re.search(pattern, email)
                pattern3 = '[a-zA-Z]'
                y = re.search(pattern3, str(name))
                pattern2 = '(\d\d\d)+\.(\d\d\d)+\.(\d\d\d\d)'
                j = re.search(pattern2, phone)
                if id == int(id) or i == None or y == None or j == None:
                    '''if i == None:
                        error_code += '+E'
                        if y == None:
                            error_code += '+N'
                            if j == None:
                                error_code += '+P'
                    '''
                    try:
                        i == None
                        error_code += '+E'
                    except:
                        pass
                    try:
                        y == None
                        error_code += '+N'
                    except:
                        pass
                    try:
                        j == None
                        error_code += '+P'
                    except:
                        pass

                    writer = csv.writer(invalid_file)
                    writer.writerow([row])
                    writer.writerow([error_code])
                else:
                    writer = csv.writer(valid_file)
                    writer.writerow([id, name, email, phone])
            except:
                error_code += 'I'




            # writer = csv.writer(valid)
            # writer.writerow([row])
            # valid_files += 1


def write_valid():
    global valid_files

    with open("valid", "w", newline='') as valid:
        writer = csv.writer(valid_file)
        #writer.writerow([row])
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
        #writer.writerow([row])
        invalid_files = invalid_files + 1




def main():
    valid_data()


if __name__ == '__main__':
    main()
