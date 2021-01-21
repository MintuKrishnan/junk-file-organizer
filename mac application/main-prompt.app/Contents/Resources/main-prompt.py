#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse_prompt import PromptParser

from organizeByDate import organize_by_date
from organizeBySize import organize_by_size
from organizeByExtension import organize_by_extension
from organizeByType import organize_by_type


def main():

    parser = PromptParser()
    parser.add_argument('-p',
                        '--path',
                        metavar='',
                        help='{path} - path of the directory to organize ')
    parser1 = PromptParser()
    parser1.add_argument(
        '-o',
        '--order',
        default='type',
        help='{extension,size,date,type} - the way you need to organize',
        metavar='',
        choices=['extension', 'size', 'date', 'type'],
    )

    path = parser.parse_args().path
    organizeBy = parser1.parse_args().order

    if organizeBy == 'extension':
        organize_by_extension(path)
    elif organizeBy == 'size':
        organize_by_size(path)
    elif organizeBy == 'date':
        organize_by_date(path)
    elif organizeBy == 'type':
        organize_by_type(path)
    else:
        print('Wrong Choice for Organizing')


if __name__ == '__main__':
    main()
