#!/usr/bin/env python3


def solve(ip):
    '''Trả về string biểu diễn binary (hệ cơ số 2) của `ip`.
    IP là một dãy gồm 4 số phân cách nhau bởi dấu `.`, mỗi số trong khoảng
    0-255.

    Input::

      192.168.1.1

    Output::

      11000000.10101000.00000001.00000001

    Python có funtion đổi số integer thành dạng binary:

      In [1]: bin(168)
      Out[1]: '0b10101000'

    Khi s = '1', s.zfill(5) sẽ thêm đủ "zero" để tạo thành '00001'
    '''
    result = ''
    ip=ip.split('.')
    ls=[]
    for i in ip:
      ls.append(bin(int(i))[2:])
    for a in range(4):
      ls[a]=ls[a].zfill(8)
    result=ls[0]+'.'+ls[1]+'.'+ls[2]+'.'+ls[3]
    return result


def main():
    '''
    Biết function `input('Bạn tên gì?')` sẽ in ra màn hình dòng chữ "Bạn tên
    gì?"
    và chờ bạn nhập câu trả lời. Sau khi bạn gõ câu trả lời rồi enter,
    nội dung bạn vừa gõ sẽ được function trả về::

      In [4]: name = input('Bạn tên gì? ')
      Bạn tên gì? Hưng

      In [5]: print(name)
      Hưng

    Note::

      Trên Python2, function tương ứng tên là `raw_input`
    '''

    # ip = input('Nhap vao ip:')
    print(solve('192.168.1.1'))


if __name__ == "__main__":
    main()
