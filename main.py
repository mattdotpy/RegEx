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

    # Open three files on to read from and two to write to
    with open("input_file", newline='') as file, open("invalid_file", "w", newline='') as invalid_file, \
            open("valid_file", "w", newline='') as valid_file:

        reader = csv.reader(file, delimiter="|")  # read the input data file
        invalid_writer = csv.writer(invalid_file)  # create writer to write to invalid data file
        valid_writer = csv.writer(valid_file)  # create writer to write to valid data file
        for row in reader:  # iterate through every row in the input data file
            try:  # try to unpack the data into its five parts
                id, name, email, phone = row
                name = name.split(', ')

            # if there aren't 5 parts or the data isn't pipe delimited write a
            # length error and add 1 to invalid_files count
            except:
                invalid_writer.writerow(['L', row])
                invalid_files = invalid_files + 1
                continue


            error_code = ''  # create an empty string to hold the error codes
            try:  # if the id is an int go to the next logic
                if id == int(id):
                    break
            except:  # if the id isn't an int give an error code of I
                error_code += 'I'

            try:
                # search the name using regex to see if it is letters then a comma then more letters
                pattern3 = '[a-zA-Z]+[,]+[a-zA-Z]'
                n = re.search(pattern3, str(name))
                # if the search doesn't return anything give an error code N and add one to invalid files count
                if n == None:
                    error_code += '+N'
                    invalid_files = invalid_files + 1
            except:  # if the search does return a correct name break
                break

            try:
                # search the email using regex to see if it matches the email format
                pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(edu)'
                e = re.search(pattern, email)
                if e == None:  # if the search returns nothing return an error code E and add 1 to the invalid count
                    error_code += '+E'
                    invalid_files = invalid_files + 1
            except:  # if the search does return a valid email then break
                break

            try:
                # search the phone number to see if it matches the phone number format
                pattern4 = '(\d\d\d)+\.(\d\d\d)+\.(\d\d\d\d)'
                p = re.search(pattern4, str(phone))
                if p == None:  # if the search returns nothing add error code P and one to the invalid count
                    error_code += '+P'
                    invalid_files = invalid_files + 1
            except:  # if the search returns a valid phone number then break
                break

            if error_code > "":  # if there are errors write the error code and the row to the invalid file
                invalid_writer.writerow([error_code, row])
            else:  # if there was no error codes write the data to the valid file and add one to the valid count
                valid_writer.writerow([id, name, email, phone])
                valid_files += 1
        print(f'Number of invalid data:  {invalid_files}')
        print(f'Number of valid data:  {valid_files}')


def main():
    validate_data()


if __name__ == '__main__':
    main()
