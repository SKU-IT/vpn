#!/usr/bin/env python3
import re
from shutil import copy2 as copy
from sys import argv

regex = re.compile('"https://www.sku\.ac\.ir/File/([^/"]*)/([^/"]*)"')


def convert(addr):
    orig_addr = addr + '~orig'
    copy(addr, orig_addr)
    with open(orig_addr, 'r') as src, open(addr, 'w') as dst:
        for line in src:
            print(regex.sub(r'"File/\2"', line), file=dst, end='')


def main():
    for file in argv[1:]:
        convert(file)


if __name__ == '__main__':
    main()
