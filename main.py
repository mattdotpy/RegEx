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


def validate_data():
    global valid_files, invalid_files

    with open("input_file", newline='') as file, open("invalid_file", "w", newline='') as invalid_file, \
            open("valid_file", "w", newline='') as valid_file:

        reader = csv.reader(file, delimiter="|")
        invalid_writer = csv.writer(invalid_file)
        valid_writer = csv.writer(valid_file)
        for row in reader:
            try:
                id, name, email, phone = row
                name = name.split(', ')
            except:
                invalid_writer.writerow(['L', row])
                invalid_files = invalid_files + 1
                continue


            error_code = ''
            try:
                if id == int(id):
                    break
            except:
                error_code += 'I'

            try:
                pattern3 = '[a-zA-Z]+[,]+[a-zA-Z]'
                n = re.search(pattern3, str(name))
                if n == None:
                    error_code += '+N'
                    invalid_files = invalid_files + 1
            except:
                break

            try:
                pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(edu)'
                e = re.search(pattern, email)
                if e == None:
                    error_code += '+E'
                    invalid_files = invalid_files + 1
            except:
                break

            try:
                pattern4 = '(\d\d\d)+\.(\d\d\d)+\.(\d\d\d\d)'
                p = re.search(pattern4, str(phone))
                if p == None:
                    error_code += '+P'
                    invalid_files = invalid_files + 1
            except:
                break

            if error_code > "":
                invalid_writer.writerow([error_code, row])
            else:
                valid_writer.writerow([id, name, email, phone])
                valid_files += 1
        print(f'Number of invalid data:  {invalid_files}')
        print(f'Number of valid data:  {valid_files}')


'''
            try:
                id == int(id)
                pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(edu)'
                i = re.search(pattern, email)
                pattern3 = '[a-zA-Z]'
                y = re.search(pattern3, str(name))
                pattern2 = '(\d\d\d)+\.(\d\d\d)+\.(\d\d\d\d)'
                j = re.search(pattern2, phone)
                if id == int(id) or i == None or y == None or j == None:
                    if i == None:
                        error_code += '+E'
                        if y == None:
                            error_code += '+N'
                            if j == None:
                                error_code += '+P'
                    
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

'''
def write_valid():
    global valid_files

    with open("valid", "w", newline='') as valid:
        # writer = csv.writer(valid_file)
        # writer.writerow([row])
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
    validate_data()


if __name__ == '__main__':
    main()
