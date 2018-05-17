#!/usr/bin/env python3

import random  # NOQA
import string  # NOQA


def your_function(length=16):
    '''Tạo một mật khẩu ngẫu nhiên (random password),
    mật khẩu này bắt buộc phải chứa ít nhất 1 chữ thường,
    1 chữ hoa, 1 số, 1 ký tự punctuation (string.punctuation).
    '''
    return(''.join(
        random.sample(string.punctuation,random.randint(0, length))+
        (list(map(str,random.sample(range(length),random.randint(0, length)))))+
        random.sample(string.ascii_lowercase,random.randint(0, length))+
        random.sample(string.ascii_uppercase,random.randint(0, length))))

def solve(input_data):
    result = your_function(input_data)
    return result


def main():
    '''
    Sinh ra 10 password và viết code đảm bảo chúng đều khác nhau.
    '''
    passwords = [your_function(12) for _ in range(10)]
    assert len(set(passwords)) != 1

    N = 12
    # print('Mậu khẩu tự tạo {0} ký tự của bạn là {1}'.format(N, solve(N)))
    print('Mat khau tu tao {0} ky tu cua ban la {1}'.format(N, solve(N)))

if __name__ == "__main__":
    main()
