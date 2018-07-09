#!/usr/bin/env python3

import random  # NOQA
import string  # NOQA


def create_pass(length):
    '''Tạo một mật khẩu ngẫu nhiên (random password),
    mật khẩu này bắt buộc phải chứa ít nhất 1 chữ thường,
    1 chữ hoa, 1 số, 1 ký tự punctuation (string.punctuation).
    '''

    password = ""
    if length > 4:
        password = [random.choice(string.ascii_lowercase) +
                    random.choice(string.ascii_uppercase) +
                    random.choice(string.digits) +
                    random.choice(string.punctuation)] +\
                            random.choices(
                                string.ascii_letters +
                                string.digits +
                                string.punctuation,
                                k=(length-4))
        return password
    if length <= 4:
        for numb in range(1, length+1):
            if numb == 1:
                password = password +\
                        random.choice(string.ascii_lowercase)

            elif numb == 2:
                password = password +\
                        random.choice(string.ascii_uppercase)

            elif numb == 3:
                password = password +\
                        random.choice(string.digits)

            elif numb == 4:
                password = password +\
                        random.choice(string.punctuation)
        return password


def generate_and_append(length, passwords=[]):
    '''
    Sinh password ngẫu nhiên và append vào list passwords.
    Nếu không có list nào được gọi với function, trả về list chứa một
    password vừa tạo ra.
    Sửa argument tùy ý.
    '''
    pass_gen = ''.join(create_pass(length))
    if passwords == []:
        return [pass_gen]
    else:
        passwords.append(pass_gen)

    return passwords


def solve(input_data):
    result = create_pass(input_data)
    return result


def main():
    '''
    Sinh ra 10 password và viết code đảm bảo chúng đều khác nhau.
    '''
    passwords8 = generate_and_append(8)
    passwords10 = generate_and_append(10)
    passwords12 = generate_and_append(12)

    passwords12 = generate_and_append(12, passwords12)

    assert len(passwords8) == 1, passwords8
    assert len(passwords10) == 1, passwords10
    assert len(passwords12) == 2, passwords12

    for ps in passwords8, passwords10, passwords12:
        for p in ps:
            plen = len(p)
            print('Mậu khẩu tự tạo {0} ký tự của bạn là {1}'.format(plen, p))


if __name__ == "__main__":
    main()
