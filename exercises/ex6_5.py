#!/usr/bin/env python3

import os
import json # NOQA


data = os.path.join(os.path.dirname(__file__), 'salt_contributors.json')


def list_contributor(datapath):
    '''Trả về list chứa các dictionary chứa data về các contributor bao gồm
    các key: login, url và contributions.
    '''
    # Sửa function cho phù hợp, trả về kết quả yêu cầu.

    with open(datapath, 'rt') as f:
        for contributor in json.load(f):
            if contributor['html_url'] == ''
            or contributor['html_url'] not in contributor:
                contributor['html_url'] = contributor['url'] + contributor['login']

            info = [{'login': contributor['login'],
                'contributions': contributor['contributions'],
                'html_url': contributor['html_url']}]
    return info

def solve(input_data):
    result = list_contributor(input_data)

    return result


def main():
    '''Truy cập đường dẫn
    https://api.github.com/repos/saltstack/salt/contributors?page=3 Lưu lại
    thành file salt_contributors.txt.
    Sử dụng JSON để chuyển dữ liệu thành dữ liệu trong Python.
    '''
    datafile = data

    print(solve(datafile))


if __name__ == "__main__":
    main()
