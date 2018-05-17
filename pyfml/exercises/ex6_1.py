#!/usr/bin/env python3

data = {'first_50': 1230, 'from_51_to_100': 1530, 'above_100': 1786}


def name(name):
    return name.title()


def calculate_cost(use, prices):
    '''Tính tiền điện (integer)
    với giá tiền cho bởi đề bài, số điện tiêu thụ `usage`
    '''
    # Viết code tính toán vào đây
    usage = int(use)
    if usage <= 50:
        return prices['first_50'] * usage
    elif 51 <= usage <= 100:
        return (prices['first_50'] * 50
                + prices['from_51_to_100'] * (usage - 50))
    else:
        return (prices['first_50'] * 50
                + prices['from_51_to_100'] * 50
                + prices['above_100'] * (usage - 100))
    pass


def solve(input_data):
    result = None

    # Bài này làm mẫu, gọi function học viên định nghĩa với input để
    # tính kết quả.
    # Các bài còn lại học viên tự định nghĩa function và gọi function để
    # tính toán kết quả `result`
    result = [(name(i[0]), calculate_cost(i[1], input_data['prices']))
              for i in input_data['usages']]

    return result


def main():
    '''
    Cho tiền điện sinh hoạt được tính theo công thức:

    - 50 số đầu: 1230 VND/số.
    - 50 số tiếp: 1530 VND/số.
    - Các số tiếp theo: 1786 VND/số.
    '''
    idata = {'usages': [1, 29, 1235, 69, 100], 'prices': data}
    print(solve(idata))


if __name__ == "__main__":
    main()
