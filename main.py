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

#FILENAME = "input.csv"


#open(FILENAME, "r")
from _csv import writer

def valid_data():
    print()


def invalid_data():
    print()


def main():
    with open("input.txt", newline="") as file:
        reader = csv.reader(file,  delimeter=",")
        for row in reader:
            print(row)


if __name__ == '__main__':
    main()
