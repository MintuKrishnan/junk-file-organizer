#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse

from beautify_cmd import beautify
from organizeByYear import organize_by_year
from organizeBySize import organize_by_size
from organizeByExtension import organize_by_extension
from organizeByType import organize_by_type
from organizeByDate import organize_by_date


def main():

    beautify()

    parser = argparse.ArgumentParser()

    parser.add_argument('-p',
                        '--path',
                        metavar='',
                        required=True,
                        help='{path} - path of the directory to organize ')

    parser.add_argument(
        '-o',
        '--order',
        default='type',
        help='{extension,size,year,type,date} - the way you need to organize',
        metavar='',
        choices=['extension', 'size', 'year', 'type', 'date'],
    )

    args = parser.parse_args()

    path = args.path
    organizeBy = args.order

    if organizeBy == 'extension':
        organize_by_extension(path)
    elif organizeBy == 'size':
        organize_by_size(path)
    elif organizeBy == 'year':
        organize_by_year(path)
    elif organizeBy == 'type':
        organize_by_type(path)
    elif organizeBy == 'date':
        organize_by_date(path)
    else:
        print('Wrong Choice for Organizing')


if __name__ == '__main__':
    main()
