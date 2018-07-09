#!/usr/bin/env python3


import os
import sys


def f_lines(f_read):
    buff_size = 1024*1024
    buff = f_read(buff_size)
    while buff:
        yield buff.count(b'\n')
        buff = f_read(buff_size)


def count_lines(file_name):
    with open(file_name, 'rb') as f:
        flines = f_lines(f.raw.read)
        lines = sum(numb for numb in flines)
        return lines


def solve(*args, **kwargs):
    '''Return tuple chứa
    - Đường dẫn tới code của module `os`
    - list chứa các attribute của os và sys
    - Số dòng trong module `os`

    Biết dir(object) sẽ trả về tất cả thuộc tính (attribute) của object đó.
    Module cũng là object.

    In [11]: import os

    In [12]: len(dir(os))
    Out[12]: 284
    '''

    result = None

    result = (os.__file__, dir(os) + dir(sys), count_lines(os.__file__))

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
