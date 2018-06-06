#!/usr/bin/env python
"""
Some excellent Python examples
"""
from pprint import pprint

FILE_NAME = 'DATA/knights.txt'

def main():
    """
    Program entry point

    :return: None
    """
    data = read_data(FILE_NAME)
    print_data(data)

def read_data(file_name):
    """
    Read data about knights.

    :param file_name: File to parse
    :return: list of knights
    """
    all_knights = []
    with open(file_name) as knights_in:
        for line in knights_in:
            fields = line.rstrip().split(':')
            all_knights.append(fields)

    return all_knights

def print_data(data):
    """
    Pretty-print the data

    :param data: List of knights
    :return: None
    """
    pprint(data)

if __name__ == '__main__':
    main()
