#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Script để nộp bài tập qua GitLab
Đặt các file bài tập trong thư mục exercises/
Chạy lệnh: python nopbai.py hcm1702_hvnex456
'''


import argparse
import shlex
import subprocess as spr


def run(cmd, skip_error=False):
    p = spr.Popen(shlex.split(cmd), stdout=spr.PIPE, stderr=spr.PIPE)
    out, err = p.communicate()
    out = out.decode().strip()
    if out:
        print(out)

    if skip_error:
        return
    else:
        if p.returncode != 0:
            raise Exception(err)


def main():
    argp = argparse.ArgumentParser()
    argp.add_argument('branch', help='Tên branch sẽ dùng để nộp bài')
    args = argp.parse_args()

    print('Đang lấy thông tin mới từ GitLab')
    run('git fetch origin master')
    run('git checkout master')
    run('git reset --hard origin/master')
    run('git checkout -b {0}'.format(args.branch), skip_error=True)
    run('git checkout {0}'.format(args.branch))
    run('git add exercises/*.py')
    run('git commit -m "{0} add exs"'.format(args.branch))
    run('git push origin {0}'.format(args.branch))
    print('Nộp bài thành công')
    print('Vào https://gitlab.com/pyfml/pyfml/merge_requests '
          'để tạo Merge Request.')


if __name__ == "__main__":
    main()
