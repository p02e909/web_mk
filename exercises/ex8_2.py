#!/usr/bin/env python3

__doc__ = '''
Yêu cầu: Viết script ex8_2.py:
- khi gọi với -h tên_file sẽ in ra 10 dòng đầu tiên của file,
- khi gọi với -t tên_file sẽ in ra 10 dòng cuối cùng của file.

Usage::

  ex8_2.py -h file_path

  -> Print 10 first lines of file_path

  ex8_2.py -t file_path

  -> Print 10 last lines of file_path

Use ``sys.argv``
'''


import subprocess
import log
import sys

logger = log.get_logger(__name__)


def list_ten_lines(option, file_path):
    '''Trả về list chứa 10 dòng tùy thuộc vào `option` (-t hoặc -h) sau khi
    đọc dữ liệu từ file

    :param option: tùy chọn để in ra các dòng đầu hoặc cuối: -h hoặc -t
    :param file_path: đường dẫn tới file
    :rtype list:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    # if os.path.isfile(file_path) == False:
    #     result = logger.debug("%s: File_not_found!", file_path)

    if option != '-h' and option != '-t':
        result = logger.debug("Unavalable_Option: %s", option)

    elif option == '-h':
        result = subprocess.getoutput('! head '+file_path).splitlines()

    elif option == '-t':
        result = subprocess.getoutput('! tail '+file_path).splitlines()

    return result


def solve(option, file_path):
    '''Hàm `solve` sử dụng với mục đích `test`, học viên không cần chỉnh
    sửa gì thêm

    :param option: tùy chọn để in ra các dòng đầu hoặc cuối: -h hoặc -t
    :param file_path: đường dẫn tới file
    :rtype list:
    '''
    # Lưu ý: sửa lại tên function của mình cho phù hợp
    logger.debug("Using %s option with file %s", option, file_path)
    result = list_ten_lines(option, file_path)

    return result


def main():
    option, file_path = None, None

    # Viết code xử lí truyền 2 argument `option` và `file_path` bên dưới
    # option: tùy chọn để in ra các dòng đầu hoặc cuối: -h hoặc -t
    # file_path: đường dẫn tới file
    # Gợi ý: sử dụng sys.argv

    sys.argv
    option = sys.argv[1]
    file_path = sys.argv[2]
    lines = solve(option, file_path)
    for line in lines:
        line = line.rstrip()
        print(line)


if __name__ == "__main__":
    main()
