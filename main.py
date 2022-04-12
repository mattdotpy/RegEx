#!/usr/bin/env python3

"""
This module contains functions to
"""

import sys
import csv

__author__ = 'Matthew Meyer'
__version__ = '1.0'
__copyright__ = "Copyright 2022.04.12, Regular Expressions"
__github__ = "https://github.com/mattdotpy/RegEx.git"

from _csv import writer


def valid_data():
    with open("input", newline='') as file, open("invalid", "w") as invalid:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            try:
                id, name, email, phone = row
                print(row)
            except:
                    writer = csv.writer(invalid)
                    writer.writerows(row)

def invalid_data():
    print()


def main():
    valid_data()


if __name__ == '__main__':
    main()
