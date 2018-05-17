#!/usr/bin/env python3

'''
Viết chương trình loại bỏ phần mở rộng của một tên file bất kỳ.

Ví dụ::

  input_data = '....slsslslsls...sls'
  output = '....slsslslsls..'

  input_data = 'maria.data.mp9'
  output = 'maria.data'
'''


def solve(input_data):
    '''Trả về tên file sau khi loại bỏ phần mở rộng

    :param input_data: tên file bất kì
    :rtype: str
    '''
    result = None

    find = input_data.rfind('.')
    result = input_data[:find]

    return result


def main():
    input_data = 'maria.data.mp9'
    print(solve(input_data))


if __name__ == "__main__":
    main()
